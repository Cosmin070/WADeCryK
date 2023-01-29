from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, session, Response, json, abort
from google.auth.exceptions import MalformedError, InvalidValue
from google.auth.transport import requests
from google.oauth2 import id_token
from flask_cors import CORS

import CryKDatabase
from config import GOOGLE_CLIENT_ID
from emailer import send_register_mail
from images import get_image, image_dict, get_response_image
from models.Cryptocurrency import Cryptocurrency
from models.Portfolio import Portfolio
from models.Profile import Profile
from models.users import User

app = Flask(__name__)
CORS(app)
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


# <editor-fold desc="images routes">
@app.route('/cryk/api/getImage/<string:name>')
def get_cryptocurrency_image(name):
    if (get_image(name)) == -1:
        return Response(status=404)
    return get_response_image(get_image(name))


@app.route('/cryk/api/getImages', methods=['POST'])
def get_crypto_image():
    if not check_user_session():
        abort(401)
    if 'images' not in request.json:
        abort(400)
    image_paths = []
    images = request.json['images']
    for image in images:
        image_paths.append(get_image(image))
    encoded_images = {}
    for image, image_path in zip(images, image_paths):
        encoded_images[image] = get_response_image(image_path)
    return jsonify(encoded_images)


@app.route('/cryk/api/cryptocurrencies/dictionary', methods=['GET'])
def get_crypto_dictionary():
    if not check_user_session():
        abort(401)
    return jsonify(image_dict)


# </editor-fold>


@app.route('/cryk/api/getVisualiaztionData', methods=['POST'])
def get_visualization_data():
    payload = request.json
    filters = payload["filters"]
    item = Cryptocurrency()
    item_list = [item]
    return jsonify(item_list)


# <editor-fold desc="authentication routes">
@app.route('/cryk/auth', methods=['POST'])
def auth():
    try:
        response = Response()
        token = request.json['token']
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        print(id_info)
    except KeyError:
        return abort(400)
    except MalformedError:
        return abort(401)
    except InvalidValue:
        session.pop('user', None)
        session.pop('id', None)
        return abort(401)
    email = id_info['email']
    user = User(email=email)
    id = CryKDatabase.insert_user(user)
    CryKDatabase.insert_user_profile(Profile(user_id=id['$oid'],
                                             firstname=id_info['given_name'],
                                             lastname=id_info['family_name'],
                                             email=id_info['email']))
    session['user'] = token
    session['id'] = id
    response.status = 200
    response.set_cookie("id", id['$oid'])
    response.data = json.dumps(id)
    return response


@app.route('/cryk/api/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    session.pop('id', None)
    resp = Response()
    resp.set_cookie('id', '', expires=0)
    return resp


@app.route('/cryk/api/login', methods=['POST'])
def login():
    response = Response()
    payload = request.json
    if 'email' not in payload or 'password' not in payload:
        abort(400)
    email = payload['email']
    password = payload['password']
    user = User(email=email, password=password)
    id = CryKDatabase.find_account(user)
    if id == -1:
        return abort(401)
    session['id'] = id
    response.set_cookie("id", id['$oid'])
    response.data = json.dumps(id)
    response.status = 200 if id != -1 else 401
    return response


@app.route('/cryk/api/register', methods=['POST'])
def register():
    if 'email' not in request.json or 'password' not in request.json:
        abort(400)
    email = request.json['email']
    password = request.json['password']
    new_user = User(email=email, password=password)
    CryKDatabase.insert_user(new_user)
    send_register_mail(new_user)
    return jsonify(succes=True)


# </editor-fold>

# <editor-fold desc="portfolio routes">
@app.route('/cryk/api/insertPortfolio', methods=['POST'])
def insert_user_portfolio():
    if not check_user_session():
        abort(401)
    if 'coins' not in request.json or any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=session['id']['$oid'], coins=request.json['coins'])
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(200)


@app.route('/cryk/api/getPortfolio')
def get_user_portfolio():
    if not check_user_session():
        abort(401)
    portfolio = CryKDatabase.get_user_portfolio(session['id']['$oid'])
    return jsonify(portfolio)


# </editor-fold>

# <editor-fold desc="profile routes">
@app.route('/cryk/api/getProfile')
def get_user_profile():
    if not check_user_session():
        abort(401)
    return jsonify(CryKDatabase.get_user_profile(session['id']['$oid']))


@app.route('/cryk/api/insertProfile', methods=['POST'])
def insert_user_profile():
    if not check_user_session():
        abort(401)
    if 'firstname' not in request.json or 'lastname' not in request.json or 'email' not in request.json:
        abort(400)
    profile = Profile(firstname=request.json['firstname'],
                      lastname=request.json['lastname'],
                      email=request.json['email'],
                      city=request.json['city'] if 'city' in request.json else "",
                      country=request.json['country'] if 'country' in request.json else "",
                      address=request.json['address'] if 'address' in request.json else "",
                      about=request.json['about'] if 'about' in request.json else "",
                      user_id=session['id']['$oid']
                      )
    if 'coins' in request.json and any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=session['id']['$oid'],
                          coins=request.json['coins'] if 'coins' in request.json else {})
    CryKDatabase.insert_user_profile(profile)
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(200)


# </editor-fold>
def check_user_session():
    if 'user' in session:
        try:
            id_token.verify_oauth2_token(session['user'], requests.Request(), GOOGLE_CLIENT_ID)
        except MalformedError:
            return False
        return True
    elif 'id' in session:
        if not CryKDatabase.is_user_in_database(session['id']['$oid']):
            return False
        return True
    return False


if __name__ == '__main__':
    app.run(port=5000)
