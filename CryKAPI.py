from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, send_file, url_for, session, Response, json, abort
from google.auth.exceptions import MalformedError
from google.auth.transport import requests
from google.oauth2 import id_token

from CryKDatabase import insert_user, find_account
from config import GOOGLE_CLIENT_ID
from emailer import send_register_mail
from images import get_image, image_dict, get_response_image
from models.Cryptocurrency import Cryptocurrency
from models.users import User

app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/cryk/api/getImages', methods=['POST'])
def get_crypto_image():
    image_paths = []
    payload = request.json
    images = payload["images"]
    for image in images:
        image_paths.append(get_image(image))
    encoded_images = {}
    for image, image_path in zip(images, image_paths):
        encoded_images[image] = get_response_image(image_path)
    return jsonify(encoded_images)


@app.route('/cryk/api/getVisualiaztionData', methods=['POST'])
def get_visualization_data():
    payload = request.json
    filters = payload["filters"]
    item = Cryptocurrency()
    item_list = [item]
    return jsonify(item_list)


@app.route('/cryk/auth', methods=['POST'])
def auth():
    try:
        response = Response()
        token = request.json['token']
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
    except KeyError:
        return abort(400)
    except MalformedError:
        return abort(401)
    email = id_info['email']
    user = User(email=email)
    id = insert_user(user)
    session['user'] = token
    session['id'] = id
    response.status = 200
    response.set_cookie("id", id['$oid'])
    response.data = json.dumps(id)
    return response


@app.route('/cryk/api/logout', methods=['GET'])
def logout():
    print(session.get('id'))
    session.pop('user', None)
    session.pop('id', None)
    resp = Response()
    resp.set_cookie('id', '', expires=0)
    return resp


@app.route('/cryk/api/login', methods=['POST'])
def login():
    response = Response()
    payload = request.json
    print(payload)
    email = payload['email']
    password = payload['password']
    user = User(email=email, password=password)
    id = find_account(user)
    response.set_cookie("id", id['$oid'])
    response.data = json.dumps(id)
    response.status = 200 if id != -1 else 401
    return response


@app.route('/cryk/api/register', methods=['POST'])
def register():
    payload = request.json
    print(payload)
    email = payload['email']
    password = payload['password']
    new_user = User(email=email, password=password)
    insert_user(new_user)
    send_register_mail(new_user)
    return jsonify(succes=True)


@app.route('/cryk/api/cryptocurrencies/dictionary', methods=['GET'])
def get_crypto_dictionary():
    return jsonify(image_dict)


if __name__ == '__main__':
    app.run(port=5000)
