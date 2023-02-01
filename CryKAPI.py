from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, request, session, Response, json, abort
from flask_cors import CORS
from google.auth.exceptions import MalformedError, InvalidValue
from google.auth.transport import requests
from google.oauth2 import id_token

import CryKDatabase
from coin_thirdparty_tool import get_custom_rate_now, get_last_days_exchange
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


@app.route('/cryk/api/getVisualizationData', methods=['POST'])
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
    response.data = json.dumps({
        "id": id['$oid'],
        "token": token
    })
    return response


@app.route('/cryk/api/logout', methods=['GET'])
def logout():
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
    if 'id' not in request.json or 'coins' not in request.json \
            or any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=request.json['id'], coins=request.json['coins'])
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(200)


@app.route('/cryk/api/getPortfolio/<string:user_id>')
def get_user_portfolio(user_id):
    if not check_user_session():
        abort(401)
    portfolio = CryKDatabase.get_user_portfolio(user_id)
    return jsonify(portfolio)


@app.route('/cryk/api/updatePortfolio/<string:user_id>', methods=['PUT'])
def update_user_portfolio(user_id):
    if 'coins' not in request.json \
            or any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=user_id, coins=request.json['coins'])
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(portfolio)


@app.route('/cryk/api/deletePortfolio/<string:user_id>', methods=['DELETE'])
def delete_user_portfolio(user_id):
    portfolio = Portfolio(user_id=user_id)
    deleted_portfolio = CryKDatabase.delete_user_portfolio(portfolio)
    return jsonify(200) if deleted_portfolio else jsonify(400)


# </editor-fold>

# <editor-fold desc="profile routes">
@app.route('/cryk/api/getProfile/<string:user_id>')
def get_user_profile(user_id):
    if not check_user_session():
        abort(401)
    return jsonify(CryKDatabase.get_user_profile(user_id))


@app.route('/cryk/api/insertProfile', methods=['POST'])
def insert_user_profile():
    if not check_user_session():
        abort(401)
    if 'firstname' not in request.json or 'lastname' not in request.json \
            or 'email' not in request.json or 'id' not in request.json:
        abort(400)
    profile = Profile(user_id=request.json['id'],
                      firstname=request.json['firstname'],
                      lastname=request.json['lastname'],
                      email=request.json['email'],
                      city=request.json['city'] if 'city' in request.json else "",
                      country=request.json['country'] if 'country' in request.json else "",
                      address=request.json['address'] if 'address' in request.json else "",
                      about=request.json['about'] if 'about' in request.json else "",
                      )
    if 'coins' in request.json and any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=request.json['id'],
                          coins=request.json['coins'] if 'coins' in request.json else {})
    CryKDatabase.insert_user_profile(profile)
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(200)


@app.route('/cryk/api/updateProfile/<string:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    if 'firstname' not in request.json or 'lastname' not in request.json \
            or 'email' not in request.json or 'id' not in request.json:
        abort(400)
    profile = Profile(user_id=user_id,
                      firstname=request.json['firstname'],
                      lastname=request.json['lastname'],
                      email=request.json['email'],
                      city=request.json['city'] if 'city' in request.json else "",
                      country=request.json['country'] if 'country' in request.json else "",
                      address=request.json['address'] if 'address' in request.json else "",
                      about=request.json['about'] if 'about' in request.json else "",
                      )
    if 'coins' in request.json and any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=user_id,
                          coins=request.json['coins'] if 'coins' in request.json else {})
    CryKDatabase.insert_user_profile(profile)
    CryKDatabase.insert_user_portfolio(portfolio)
    return jsonify(200)


@app.route('/cryk/api/deleteProfile/<string:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    if 'firstname' not in request.json or 'lastname' not in request.json \
            or 'email' not in request.json or 'id' not in request.json:
        abort(400)
    profile = Profile(user_id=user_id,
                      firstname=request.json['firstname'],
                      lastname=request.json['lastname'],
                      email=request.json['email'],
                      city=request.json['city'] if 'city' in request.json else "",
                      country=request.json['country'] if 'country' in request.json else "",
                      address=request.json['address'] if 'address' in request.json else "",
                      about=request.json['about'] if 'about' in request.json else "",
                      )
    if 'coins' in request.json and any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    portfolio = Portfolio(user_id=user_id,
                          coins=request.json['coins'] if 'coins' in request.json else {})
    deleted_profile = CryKDatabase.delete_user_profile(profile)
    deleted_portfolio = CryKDatabase.delete_user_portfolio(portfolio)
    if deleted_portfolio and deleted_profile:
        return jsonify(200)
    return jsonify(400)


# </editor-fold>


# <editor-fold desc="coins routes">
@app.route('/cryk/api/getCurrentPriceForCoin/<string:coin>', methods=['GET'])
def get_current_price_for_coin(coin: str):
    # if not check_user_session():
    #     abort(401)
    result = get_custom_rate_now(coin)
    if result == -1:
        abort(400)
    if result == -2:
        abort(404)
    return jsonify(result)


@app.route('/cryk/api/getHistoricalPriceForCoin', methods=['GET'])
def get_historical_prices_for_coin():
    # if not check_user_session():
    #     abort(401)
    coin = request.args.get('coin', None)
    days = request.args.get('days', None)
    if coin is None or days is None or not days.isdigit() or int(days) > 5:
        abort(400)
    result = get_last_days_exchange(coin, int(days))
    if result == -1:
        abort(400)
    if result == -2:
        abort(404)
    return jsonify(result)


# </editor-fold>


def check_user_session():
    if 'token' in request.headers:
        try:
            id_token.verify_oauth2_token(request.headers['token'], requests.Request(), GOOGLE_CLIENT_ID)
        except MalformedError:
            return False
        return True
    elif 'id' in session:
        if not CryKDatabase.is_user_in_database(request.headers['id']):
            return False
        return True
    return False


if __name__ == '__main__':
    app.run(port=5000)
