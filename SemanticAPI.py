from flask import Flask, jsonify, request, abort
from flask_cors import CORS

import ontology
from images import image_dict
from models.Cryptocurrency import Cryptocurrency
from ontology import get_cryptocurrencies_by_protocol_from_ontology, get_cryptocurrency_details_from_ontology, \
    perform_query_on_ontology, get_cryptocurrencies_details_from_ontology
from utils.compute_useful_coins import coins

app = Flask(__name__)
CORS(app)


@app.route('/ontology/api/cryptocurrencies')
def get_all_cryptocurrencies():
    protocol = request.args.get('protocol', None)
    if protocol is None:
        all_coins = [coin['name'].lower() for coin in coins]
        return jsonify(get_cryptocurrencies_details_from_ontology(all_coins))
    if protocol not in ["pos", "pow"]:
        abort(400)
    if protocol == "pos":
        return jsonify(get_cryptocurrencies_by_protocol_from_ontology("pos"))
    return jsonify(get_cryptocurrencies_by_protocol_from_ontology("pow"))


@app.route('/ontology/api/cryptocurrency')
def get_cryptocurrency_details():
    identifier = request.args.get('name', None)
    if identifier is None:
        abort(400)
    if identifier not in image_dict:
        abort(400)
    return jsonify(get_cryptocurrency_details_from_ontology(identifier))


@app.route('/ontology/api/cryptocurrenciesByName', methods=['POST'])
def get_cryptocurrencies_details():
    if 'coins' not in request.json or any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    return jsonify(get_cryptocurrencies_details_from_ontology(request.json['coins']))


@app.route('/ontology/api/runQuery', methods=['POST'])
def run_query():
    print(request.json)
    if 'query' not in request.json:
        abort(400)
    return jsonify(perform_query_on_ontology(request.json['query']))


@app.route('/ontology/api/<string:rformat>/getCryptocurrencies')
def get_all_cryptocurrencies_from_jsonld(rformat):
    if rformat not in ['json-ld', 'html-rdfa']:
        abort(400)
    if rformat == 'json-ld':
        return jsonify(ontology.get_all_cryptocurrencies_from_jsonld())
    if rformat == 'html-rdfa':
        return ontology.get_all_cryptocurrencies_from_jsonld_as_html_rdfa()


@app.route('/ontology/api/<string:rformat>/getCryptocurrenciesByName', methods=['POST'])
def get_cryptocurrencies_by_name_from_jsonld(rformat):
    if rformat not in ['json-ld', 'html-rdfa']:
        abort(400)
    if 'coins' not in request.json or any([False if coin in image_dict else True for coin in request.json['coins']]):
        abort(400)
    if rformat == 'json-ld':
        return jsonify(ontology.get_cryptocurrencies_from_jsonld(request.json['coins']))
    if rformat == 'html-rdfa':
        return ontology.get_cryptocurrencies_from_jsonld_as_html_rdfa(request.json['coins'])


if __name__ == '__main__':
    app.run(port=5001)
