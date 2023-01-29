import io
import json
from typing import Dict, Any

import rdflib
from rdflib import URIRef, Literal, BNode
from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer
from rdflib.query import ResultException

from models.Cryptocurrency import Cryptocurrency

g = rdflib.Graph()
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
                    ?x dc:description ?description .
                    ?x doacc:block-time ?block_time .
                    ?x doacc:date-founded ?date_founded .
                    ?x doacc:incept ?incept .
                    ?x doacc:protection-scheme ?protection_scheme .   
                    ?x doacc:source ?source .
                    ?x doacc:protocol ?protocol .   
                    ?x doacc:symbol ?symbol .
                    ?x doacc:total-coins ?total_coins .
                    
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
                                               description=cryptocurrency[1].toPython(),
                                               block_time=cryptocurrency[2].toPython(),
                                               date_founded=cryptocurrency[3].toPython(),
                                               incept=cryptocurrency[4].toPython(),
                                               protection_scheme=cryptocurrency[5].toPython(),
                                               source=cryptocurrency[6].toPython(),
                                               protocol=cryptocurrency[7].toPython(),
                                               symbol=cryptocurrency[8].toPython(),
                                               total_coins=cryptocurrency[9].toPython(),
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


def get_cryptocurrencies_details_from_ontology(coins):
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
                    ?x dc:description ?description .
                    ?x doacc:block-time ?block_time .
                    ?x doacc:date-founded ?date_founded .
                    ?x doacc:incept ?incept .
                    ?x doacc:protection-scheme ?protection_scheme .   
                    ?x doacc:source ?source .
                    ?x doacc:protocol ?protocol .   
                    ?x doacc:symbol ?symbol .
                    ?x doacc:total-coins ?total_coins .
                    
                    Optional {{
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
                    FILTER regex(?name, "^{build_query_parameter(coins)}$", "i")

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
                                               protection_scheme=cryptocurrency[5].toPython(),
                                               source=cryptocurrency[6].toPython(),
                                               protocol=cryptocurrency[7].toPython(),
                                               symbol=cryptocurrency[8].toPython(),
                                               total_coins=cryptocurrency[9].toPython(),
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


def build_query_parameter(coins):
    query = ''
    coins = set(coins)
    for coin in coins:
        query += coin + '$|'
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
