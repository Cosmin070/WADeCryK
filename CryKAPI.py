from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, send_file, url_for, session, redirect

# from CryKDatabase import __get_database
from Cryptocurrency import Cryptocurrency

# db = __get_database()
# print(db)

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
    session['user'] = token['userinfo']
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5002)
