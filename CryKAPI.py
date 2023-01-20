from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, send_file, url_for, session, redirect, make_response

from CryKDatabase import insert_user
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
    return send_file("images/D/dogecoin_doge.png", mimetype='image/png')


@app.route('/cryk/api/getVisualiaztionData', methods=["POST"])
def get_visualization_data():
    payload = request.json
    filters = payload["filters"]
    item = Cryptocurrency()
    item_list = [item]
    return jsonify(item_list)


@app.route('/cryk/api/login')
def login():
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


@app.route('/logout')
def logout():
    print(session.get('id'))
    session.pop('id', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5000)
