from os import abort

from flask import Flask, jsonify, request, send_file

from Cryptocurrency import Cryptocurrency

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port=5002)

