from flask import Flask, jsonify, request, abort

from images import image_dict
from models.Cryptocurrency import Cryptocurrency
from ontology import get_cryptocurrencies_by_protocol_from_ontology, get_cryptocurrency_details_from_ontology, \
    perform_query_on_ontology, get_cryptocurrencies_details_from_ontology
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/ontology/api/cryptocurrencies')
def get_all_cryptocurrencies():
    cryptocurrencies = get_cryptocurrencies_by_protocol_from_ontology("pos")
    cryptocurrencies.append(get_cryptocurrencies_by_protocol_from_ontology("pow"))
    return jsonify(cryptocurrencies)


@app.route('/ontology/api/cryptocurrenciesByYears', methods=["POST"])
def get_cryptocurrencies_by_year():
    from_year, to_year = None, None
    payload = request.json
    if "period" in payload:
        period = payload["period"]
        from_year = period["from_year"]
        if "to_year" in period:
            to_year = period["to_year"]
    print(from_year, to_year)
    item = Cryptocurrency(date_founded=from_year)
    item_list = [item]
    return jsonify(item_list)


@app.route('/ontology/api/<string:protocol>/cryptocurrencies')
def get_cryptocurrencies_by_protocol(protocol):
    if protocol not in ["pos", "pow"]:
        abort(400)
    if protocol == "pos":
        return jsonify(get_cryptocurrencies_by_protocol_from_ontology("pos"))
    return jsonify(get_cryptocurrencies_by_protocol_from_ontology("pow"))


@app.route('/ontology/api/cryptocurrencyByName/<string:identifier>')
def get_cryptocurrency_details(identifier):
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


if __name__ == '__main__':
    app.run(port=5001)
