import json
from typing import Dict, Any

from rdflib import Graph
from rdflib import URIRef, Literal, BNode
from rdflib.query import ResultException

from constants.ontology_constants import LABEL, SYMBOL, PREMINE, POW, POS, WEBSITE, TOTAL_COINS, PROTOCOL, \
    PROTECTION_SCHEME, INCEPT, DATE_FOUNDED, BLOCK_TIME, DESCRIPTION, SOURCE
from models.Cryptocurrency import Cryptocurrency
from utils.compute_useful_coins import coins

g = Graph()
g.parse("utils/cryptocurrency.jsonld")


def get_cryptocurrencies_by_protocol_from_ontology(consensus):
    coin_names = [coin['name'].lower() for coin in coins]
    filtered_coins = [coin for coin in coins if coin['name'].lower() in coin_names]
    symbols = [coin["symbol"] for coin in filtered_coins]
    result = g.query(
        f"""
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX ccy: <http://purl.org/net/bel-epa/ccy#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX doacc: <http://purl.org/net/bel-epa/doacc#>
            
            SELECT ?name ?consensus ?description ?block_time ?date_founded ?incept
                    ?protection_scheme
                    ?source ?protocol ?symbol ?total_coins ?website 
                    ?premine
                WHERE {{
                    ?x skos:prefLabel ?name .
                    ?x doacc:{consensus} ?consensus .
                    OPTIONAL {{
                        ?x dc:description ?description .
                    }}
                    OPTIONAL {{
                        ?x doacc:block-time ?block_time .
                    }}
                    OPTIONAL {{
                        ?x doacc:date-founded ?date_founded .
                    }}
                    OPTIONAL {{
                        ?x doacc:incept ?incept .
                    }}
                    OPTIONAL {{
                        ?x doacc:protection-scheme ?protection_scheme .  
                    }} 
                    OPTIONAL {{
                        ?x doacc:source ?source .
                    }}
                    OPTIONAL {{
                        ?x doacc:protocol ?protocol .
                    }}
                    OPTIONAL {{
                        ?x doacc:symbol ?symbol .
                    }}
                    OPTIONAL{{
                        ?x doacc:total-coins ?total_coins .
                    }}
                    OPTIONAL {{
                        ?x doacc:website ?website .
                    }}
                    OPTIONAL{{
                        ?x doacc:premine ?premine .
                    }}
                    FILTER regex(?name, "^{build_query_parameter(coin_names)}", "i")
                    FILTER regex(?symbol, "^{build_query_parameter(symbols)}", "i")
                }}
    """
    )
    cryptocurrencies = []
    for cryptocurrency in result:
        cryptocurrencies.append(Cryptocurrency(name=cryptocurrency[0].toPython(),
                                               proof_of_work=cryptocurrency[1].toPython()
                                               if consensus == "pow" else "",
                                               proof_of_stake=cryptocurrency[1].toPython()
                                               if consensus == "pos" else "",
                                               description=cryptocurrency[2].toPython()
                                               if cryptocurrency[2] is not None else "",
                                               block_time=cryptocurrency[3].toPython()
                                               if cryptocurrency[3] is not None else "",
                                               date_founded=cryptocurrency[4].toPython()
                                               if cryptocurrency[4] is not None else "",
                                               incept=cryptocurrency[5].toPython()
                                               if cryptocurrency[5] is not None else "",
                                               protection_scheme=cryptocurrency[6].toPython()
                                               if cryptocurrency[6] is not None else "",
                                               source=cryptocurrency[7].toPython()
                                               if cryptocurrency[7] is not None else "",
                                               protocol=cryptocurrency[8].toPython()
                                               if cryptocurrency[8] is not None else "",
                                               symbol=cryptocurrency[9].toPython()
                                               if cryptocurrency[9] is not None else "",
                                               total_coins=cryptocurrency[10].toPython()
                                               if cryptocurrency[10] is not None else "",
                                               website=cryptocurrency[11].toPython()
                                               if cryptocurrency[11] is not None else "",
                                               premine=cryptocurrency[12].toPython()
                                               if cryptocurrency[12] is not None else "",
                                               ))
    return cryptocurrencies


def get_cryptocurrency_details_from_ontology(identifier):
    symbols = [coin["symbol"] for coin in coins if coin['name'].lower() == identifier]
    result = g.query(
        f"""
                PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                PREFIX ccy: <http://purl.org/net/bel-epa/ccy#>
                PREFIX dc: <http://purl.org/dc/elements/1.1/>
                PREFIX doacc: <http://purl.org/net/bel-epa/doacc#>

                SELECT ?name ?description ?block_time ?date_founded ?incept
                    ?protection_scheme
                    ?source ?protocol ?symbol ?total_coins ?website 
                    ?pos ?pow ?premine
                WHERE {{
                    ?x skos:prefLabel ?name .
                    OPTIONAL {{
                        ?x dc:description ?description .
                    }}
                    OPTIONAL {{
                        ?x doacc:block-time ?block_time .
                    }}
                    OPTIONAL {{
                        ?x doacc:date-founded ?date_founded .
                    }}
                    OPTIONAL {{
                        ?x doacc:incept ?incept .
                    }}
                    OPTIONAL {{
                        ?x doacc:protection-scheme ?protection_scheme .  
                    }} 
                    OPTIONAL {{
                        ?x doacc:source ?source .
                    }}
                    OPTIONAL {{
                        ?x doacc:protocol ?protocol .
                    }}
                    OPTIONAL {{
                        ?x doacc:symbol ?symbol .
                    }}
                    OPTIONAL{{
                        ?x doacc:total-coins ?total_coins .
                    }}
                    OPTIONAL {{
                        ?x doacc:website ?website .
                    }}
                    OPTIONAL{{
                        ?x doacc:pos ?pos .
                    }} .
                    OPTIONAL{{
                        ?x doacc:pow ?pow .
                    }} .
                    OPTIONAL{{
                        ?x doacc:premine ?premine .
                    }} .
                    FILTER regex(?name, "^{identifier}$", "i")
                    FILTER regex(?symbol, "^{build_query_parameter(symbols)}", "i")
                }}
        """
    )
    cryptocurrencies = []
    for cryptocurrency in result:
        cryptocurrencies.append(Cryptocurrency(name=cryptocurrency[0].toPython(),
                                               description=cryptocurrency[1].toPython()
                                               if cryptocurrency[1] is not None else "",
                                               block_time=cryptocurrency[2].toPython()
                                               if cryptocurrency[2] is not None else "",
                                               date_founded=cryptocurrency[3].toPython()
                                               if cryptocurrency[3] is not None else "",
                                               incept=cryptocurrency[4].toPython()
                                               if cryptocurrency[4] is not None else "",
                                               protection_scheme=cryptocurrency[5].toPython()
                                               if cryptocurrency[5] is not None else "",
                                               source=cryptocurrency[6].toPython()
                                               if cryptocurrency[6] is not None else "",
                                               protocol=cryptocurrency[7].toPython()
                                               if cryptocurrency[7] is not None else "",
                                               symbol=cryptocurrency[8].toPython()
                                               if cryptocurrency[8] is not None else "",
                                               total_coins=cryptocurrency[9].toPython()
                                               if cryptocurrency[9] is not None else "",
                                               website=cryptocurrency[10].toPython()
                                               if cryptocurrency[10] is not None else "",
                                               proof_of_stake=cryptocurrency[11].toPython()
                                               if cryptocurrency[11] is not None else "",
                                               proof_of_work=cryptocurrency[12].toPython()
                                               if cryptocurrency[12] is not None else "",
                                               premine=cryptocurrency[13].toPython()
                                               if cryptocurrency[13] is not None else "",
                                               ))
    return cryptocurrencies


def get_cryptocurrencies_details_from_ontology(coin_names):
    coin_names = [coin.lower() for coin in coin_names]
    filtered_coins = [coin for coin in coins if coin['name'].lower() in coin_names]
    symbols = [coin["symbol"] for coin in filtered_coins]
    result = g.query(
        f"""
                PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                PREFIX ccy: <http://purl.org/net/bel-epa/ccy#>
                PREFIX dc: <http://purl.org/dc/elements/1.1/>
                PREFIX doacc: <http://purl.org/net/bel-epa/doacc#>

                SELECT 
                    ?name ?description ?block_time ?date_founded ?incept
                    ?protection_scheme
                    ?source ?protocol ?symbol ?total_coins ?website
                    ?pos ?pow ?premine
                WHERE {{ 
                    ?x skos:prefLabel ?name .
                    OPTIONAL {{
                        ?x dc:description ?description .
                    }}
                    OPTIONAL {{
                        ?x doacc:block-time ?block_time .
                    }}
                    OPTIONAL {{
                        ?x doacc:date-founded ?date_founded .
                    }}
                    OPTIONAL {{
                        ?x doacc:incept ?incept .
                    }}
                    OPTIONAL {{
                        ?x doacc:protection-scheme ?protection_scheme .
                    }}
                    OPTIONAL {{
                        ?x doacc:source ?source .
                    }}
                    OPTIONAL {{
                        ?x doacc:protocol ?protocol .
                    }}
                    OPTIONAL {{
                        ?x doacc:symbol ?symbol .
                    }}
                    OPTIONAL{{
                        ?x doacc:total-coins ?total_coins .
                    }}
                    OPTIONAL {{
                        ?x doacc:website ?website .
                    }}
                    OPTIONAL{{
                        ?x doacc:pos ?pos .
                    }} .
                    OPTIONAL{{
                        ?x doacc:pow ?pow .
                    }} .
                    OPTIONAL{{
                        ?x doacc:premine ?premine .
                    }} .
                    FILTER regex(?name, "^{build_query_parameter(coin_names)}$", "i")
                    FILTER regex(?symbol, "^{build_query_parameter(symbols)}$", "i")

                }}
        """
    )
    cryptocurrencies = []
    for cryptocurrency in result:
        cryptocurrencies.append(Cryptocurrency(name=cryptocurrency[0].toPython(),
                                               description=cryptocurrency[1].toPython()
                                               if cryptocurrency[1] is not None else "",
                                               block_time=cryptocurrency[2].toPython()
                                               if cryptocurrency[2] is not None else "",
                                               date_founded=cryptocurrency[3].toPython()
                                               if cryptocurrency[3] is not None else "",
                                               incept=cryptocurrency[4].toPython()
                                               if cryptocurrency[4] is not None else "",
                                               protection_scheme=cryptocurrency[5].toPython()
                                               if cryptocurrency[5] is not None else "",
                                               source=cryptocurrency[6].toPython()
                                               if cryptocurrency[6] is not None else "",
                                               protocol=cryptocurrency[7].toPython()
                                               if cryptocurrency[7] is not None else "",
                                               symbol=cryptocurrency[8].toPython()
                                               if cryptocurrency[8] is not None else "",
                                               total_coins=cryptocurrency[9].toPython()
                                               if cryptocurrency[9] is not None else "",
                                               website=cryptocurrency[10].toPython()
                                               if cryptocurrency[10] is not None else "",
                                               proof_of_stake=cryptocurrency[11].toPython()
                                               if cryptocurrency[11] is not None else "",
                                               proof_of_work=cryptocurrency[12].toPython()
                                               if cryptocurrency[12] is not None else "",
                                               premine=cryptocurrency[13].toPython()
                                               if cryptocurrency[13] is not None else "",
                                               ))
    return cryptocurrencies


def perform_query_on_ontology(query):
    try:
        result = g.query(query)
        serialize(result)
        return serialize(result)
    except Exception as e:
        print(e)
    return 1


def build_query_parameter(parameters):
    query = ''
    parameters = set(parameters)
    for parameter in parameters:
        query += parameter + '$|'
    return query[:-1]


def serialize(result):
    res: Dict[str, Any] = {}
    if result.type == "ASK":
        res["head"] = {}
        res["boolean"] = result.askAnswer
    else:
        res["results"] = {}
        res["head"] = {}
        res["head"]["vars"] = result.vars
        res["results"]["bindings"] = [
            binding_to_json(x) for x in result.bindings
        ]
    return res


def binding_to_json(b):
    res = {}
    for var in b:
        j = term_to_json(b[var])
        if j is not None:
            res[var] = term_to_json(b[var])
    return res


def term_to_json(term):
    if isinstance(term, URIRef):
        return {"type": "uri", "value": str(term)}
    elif isinstance(term, Literal):
        r = {"type": "literal", "value": str(term)}

        if term.datatype is not None:
            r["datatype"] = str(term.datatype)
        if term.language is not None:
            r["xml:lang"] = term.language
        return r

    elif isinstance(term, BNode):
        return {"type": "bnode", "value": str(term)}
    elif term is None:
        return None
    else:
        raise ResultException("Unknown term type: %s (%s)" % (term, type(term)))


def get_cryptocurrencies_from_jsonld(coin_names):
    coin_names = [coin.lower() for coin in coin_names]
    filtered_coins = [coin for coin in coins if coin['name'].lower() in coin_names]
    labels = [coin['name'].lower() for coin in filtered_coins]
    symbols = [coin["symbol"].lower() for coin in filtered_coins]
    f = open('utils/cryptocurrency.jsonld', encoding='utf-8')
    data = json.load(f)
    result = [x for x in data if
              LABEL in x
              and x[LABEL][0]['@value'].lower() in labels
              and SYMBOL in x
              and x[SYMBOL][0]['@value'].lower() in symbols]
    return result


def get_all_cryptocurrencies_from_jsonld():
    coin_names = [coin['name'].lower() for coin in coins]
    filtered_coins = [coin for coin in coins if coin['name'].lower() in coin_names]
    labels = [coin['name'].lower() for coin in filtered_coins]
    symbols = [coin["symbol"].lower() for coin in filtered_coins]
    f = open('utils/cryptocurrency.jsonld', encoding='utf-8')
    data = json.load(f)
    result = [x for x in data if
              LABEL in x
              and x[LABEL][0]['@value'].lower() in labels
              and SYMBOL in x
              and x[SYMBOL][0]['@value'].lower() in symbols]
    return result


def get_cryptocurrencies_from_jsonld_as_html_rdfa(coin_names):
    return generate_html_rdfa(get_cryptocurrencies_from_jsonld(coin_names))


def get_all_cryptocurrencies_from_jsonld_as_html_rdfa():
    return generate_html_rdfa(get_all_cryptocurrencies_from_jsonld())


def generate_html_rdfa(result):
    html_rdfa_response = """
            <div    xmlns:ps="http://www.w3.org/2004/02/skos/core#"
                    xmlns:doacc="http://purl.org/net/bel-epa/doacc#">
        """
    for coin in result:
        if LABEL in coin:
            html_rdfa_response += f'<span property="skos:prefLabel"><b>{coin[LABEL][0]["@value"]}</b></span><br>'
        if DESCRIPTION in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:description">Description: {coin[DESCRIPTION][0]["@value"]}</span><br>'
        if BLOCK_TIME in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:block-time">Block time: {coin[BLOCK_TIME][0]["@value"]}</span><br>'
        if DATE_FOUNDED in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:date-founded">Date founded: {coin[DATE_FOUNDED][0]["@value"]}</span><br>'
        if INCEPT in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:incept">Incept: {coin[INCEPT][0]["@value"]}</span><br>'
        if PROTECTION_SCHEME in coin:
            if "http" in coin[PROTECTION_SCHEME][0]["@id"]:
                html_rdfa_response += f'&emsp;Protection scheme: <a property="doacc:protection-scheme" href="{coin[PROTECTION_SCHEME][0]["@id"]}">{coin[PROTECTION_SCHEME][0]["@id"]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:protection-scheme">Protection scheme: {coin[PROTECTION_SCHEME][0]["@id"]}</span><br>'
        if SOURCE in coin:
            field = "@id" if "@id" in coin[SOURCE][0] else "@value"
            if "http" in coin[SOURCE][0][field]:
                html_rdfa_response += f'&emsp;Source: <a property="doacc:source" href="{coin[SOURCE][0][field]}">{coin[SOURCE][0][field]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:source">Source: {coin[SOURCE][0][field]}</span><br>'
        if PROTOCOL in coin:
            field = "@id" if "@id" in coin[PROTOCOL][0] else "@value"
            if "http" in coin[PROTOCOL][0][field]:
                html_rdfa_response += f'&emsp;Protocol: <a property="doacc:protocol" href="{coin[PROTOCOL][0][field]}">{coin[PROTOCOL][0][field]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:protocol">Protocol: {coin[PROTOCOL][0][field]}</span><br>'
        if SYMBOL in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:symbol">Symbol: {coin[SYMBOL][0]["@value"]}</span><br>'
        if TOTAL_COINS in coin:
            html_rdfa_response += f'&emsp;<span property="doacc:total-coins">Total coins: {coin[TOTAL_COINS][0]["@value"]}</span><br>'
        if WEBSITE in coin:
            field = "@id" if "@id" in coin[WEBSITE][0] else "@value"
            if "http" in coin[WEBSITE][0][field]:
                html_rdfa_response += f'&emsp;Website: <a property="doacc:website" href="{coin[WEBSITE][0][field]}">{coin[WEBSITE][0][field]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:website">Website: {coin[WEBSITE][0][field]}</span><br>'
        if POS in coin:
            if "http" in coin[POS][0]["@id"]:
                html_rdfa_response += f'&emsp;POS: <a property="doacc:pos" href="{coin[POS][0]["@id"]}">{coin[POS][0]["@id"]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:pos">POS: {coin[POS][0]["@id"]}</span><br>'
        if POW in coin:
            if "http" in coin[POW][0]["@id"]:
                html_rdfa_response += f'&emsp;POW: <a property="doacc:pow" href="{coin[POW][0]["@id"]}">{coin[POW][0]["@id"]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:pow">POW: {coin[POW][0]["@id"]}</span><br>'
        if PREMINE in coin:
            if "http" in coin[PREMINE][0]["@value"]:
                html_rdfa_response += f'&emsp;Premine: <a property="doacc:premine" href="{coin[PREMINE][0]["@value"]}">{coin[PREMINE][0]["@value"]}</a><br>'
            else:
                html_rdfa_response += f'&emsp;<span property="doacc:premine">Premine: {coin[PREMINE][0]["@value"]}</span><br>'
    html_rdfa_response += "</div>"
    return html_rdfa_response
