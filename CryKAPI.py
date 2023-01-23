from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, send_file, url_for, session, redirect, Response, json

from CryKDatabase import insert_user, find_account
from emailer import send_register_mail
from images import get_image
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


@app.route('/cryk/api/getImage/<string:name>')
def get_cryptocurrency_image(name):
    if (get_image(name)) == -1:
        return Response(status=404)
    return send_file(get_image(name), mimetype='image/png')


@app.route('/cryk/api/getVisualiaztionData', methods=['POST'])
def get_visualization_data():
    payload = request.json
    filters = payload["filters"]
    item = Cryptocurrency()
    item_list = [item]
    return jsonify(item_list)


@app.route('/cryk/api/glogin')
def glogin():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/cryk/auth')
def auth():
    token = oauth.google.authorize_access_token()
    email = token['userinfo']['email']
    user = User(email=email)
    id = insert_user(user)
    session['user'] = token['userinfo']
    session['id'] = id
    return redirect("/")


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


if __name__ == '__main__':
    app.run(port=5000)
