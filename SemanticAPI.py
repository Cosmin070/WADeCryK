from flask import Flask, jsonify, request, abort

from Cryptocurrency import Cryptocurrency

app = Flask(__name__)


@app.route('/ontology/api/cryptocurrencies')
def get_all_cryptocurrencies():
    item = Cryptocurrency()
    item_list = [item]
    return jsonify(item_list)


@app.route('/ontology/api/cryptocurrenciesById', methods=["POST"])
def get_cryptocurrencies_by_id():
    ids = None
    payload = request.json
    if "ids" in payload:
        ids = payload["ids"]
    print(ids)
    item = Cryptocurrency(crypto_id=ids[0])
    item_list = [item]
    return jsonify(item_list)


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


@app.route('/ontology/api/cryptocurrencies/<int:id>')
def get_cryptocurrency_by_id(_id):
    item = Cryptocurrency(crypto_id=_id)
    item_list = [item]
    return jsonify(item_list)


@app.route('/ontology/api/<string:protocol>/cryptocurrencies')
def get_cryptocurrency_by_protocol(protocol):
    if protocol not in ["pos", "pow"]:
        abort(400)
    item = Cryptocurrency(protocol=protocol)
    item_list = [item]
    return jsonify(item_list)


if __name__ == '__main__':
    app.run(port=5001)
