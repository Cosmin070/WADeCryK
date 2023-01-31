import json
from typing import Dict, Any

from rdflib import Graph
from rdflib import URIRef, Literal, BNode
from rdflib.query import ResultException

from models.Cryptocurrency import Cryptocurrency
from utils.compute_useful_coins import coins

g = Graph()
g.parse("utils/cryptocurrency.jsonld")


def get_cryptocurrencies_by_protocol_from_ontology(consensus):
    result = g.query(
        f"""
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX ccy: <http://purl.org/net/bel-epa/ccy#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX doacc: <http://purl.org/net/bel-epa/doacc#>

            SELECT ?name ?description ?block_time ?date_founded ?incept
                ?consensus ?protection_scheme
                ?source ?protocol ?symbol ?total_coins ?website ?premine
            WHERE {{
                ?x skos:prefLabel ?name .
                ?x dc:description ?description .
                ?x doacc:block-time ?block_time .
                ?x doacc:date-founded ?date_founded .
                ?x doacc:incept ?incept .
                ?x doacc:{consensus} ?consensus .
                ?x doacc:protection-scheme ?protection_scheme .   
                ?x doacc:source ?source .
                ?x doacc:protocol ?protocol .   
                ?x doacc:symbol ?symbol .
                ?x doacc:total-coins ?total_coins .
                OPTIONAL {{
                    ?x doacc:website ?website .
                }}
                OPTIONAL{{
                        ?x doacc:premine ?premine .
                }} .
            }}
    """
    )
    cryptocurrencies = []
    for cryptocurrency in result:
        cryptocurrencies.append(Cryptocurrency(name=cryptocurrency[0].toPython(),
                                               description=cryptocurrency[1].toPython(),
                                               block_time=cryptocurrency[2].toPython(),
                                               date_founded=cryptocurrency[3].toPython(),
                                               incept=cryptocurrency[4].toPython(),
                                               proof_of_work=cryptocurrency[5].toPython()
                                               if consensus == "pow" else "",
                                               proof_of_stake=cryptocurrency[5].toPython()
                                               if consensus == "pos" else "",
                                               protection_scheme=cryptocurrency[6].toPython(),
                                               source=cryptocurrency[7].toPython(),
                                               protocol=cryptocurrency[8].toPython(),
                                               symbol=cryptocurrency[9].toPython(),
                                               total_coins=cryptocurrency[10].toPython(),
                                               website=cryptocurrency[11].toPython()
                                               if cryptocurrency[11] is not None else "",
                                               premine=cryptocurrency[12].toPython()
                                               if cryptocurrency[12] is not None else "",
                                               ))
    return cryptocurrencies


def get_cryptocurrency_details_from_ontology(identifier):
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
                    ?id ?name ?description ?block_time ?date_founded ?incept
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
    symbols = [coin["symbol"].lower() for coin in filtered_coins]
    f = open('utils/cryptocurrency.jsonld', encoding='utf-8')
    data = json.load(f)
    result = [x for x in data if
              'http://www.w3.org/2004/02/skos/core#prefLabel' in x
              and x['http://www.w3.org/2004/02/skos/core#prefLabel'][0]['@value'].lower() in coin_names
              and 'http://purl.org/net/bel-epa/doacc#symbol' in x
              and x['http://purl.org/net/bel-epa/doacc#symbol'][0]['@value'].lower() in symbols]
    return result


def get_all_cryptocurrencies_from_jsonld():
    f = open('utils/cryptocurrency.jsonld', encoding='utf-8')
    data = json.load(f)
    return data
