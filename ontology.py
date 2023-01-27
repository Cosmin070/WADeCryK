import rdflib

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
                ?consensus ?premine ?protection_scheme
                ?source ?protocol ?symbol ?total_coins ?website
            WHERE {{
                ?x skos:prefLabel ?name .
                ?x dc:description ?description .
                ?x doacc:block-time ?block_time .
                ?x doacc:date-founded ?date_founded .
                ?x doacc:incept ?incept .
                ?x doacc:{consensus} ?consensus .
                ?x doacc:premine ?premine  .
                ?x doacc:protection-scheme ?protection_scheme .   
                ?x doacc:source ?source .
                ?x doacc:protocol ?protocol .   
                ?x doacc:symbol ?symbol .
                ?x doacc:total-coins ?total_coins .
                ?x doacc:website ?website .
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
                                               premine=cryptocurrency[6].toPython(),
                                               protection_scheme=cryptocurrency[7].toPython(),
                                               source=cryptocurrency[8].toPython(),
                                               protocol=cryptocurrency[9].toPython(),
                                               symbol=cryptocurrency[10].toPython(),
                                               total_coins=cryptocurrency[11].toPython(),
                                               website=cryptocurrency[12].toPython()
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
                    ?x doacc:website ?website .
                    
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
                                               website=cryptocurrency[10].toPython(),
                                               proof_of_stake=cryptocurrency[11].toPython()
                                               if cryptocurrency[11] is not None else "",
                                               proof_of_work=cryptocurrency[12].toPython()
                                               if cryptocurrency[12] is not None else "",
                                               premine=cryptocurrency[13].toPython()
                                               if cryptocurrency[13] is not None else "",
                                               ))
    return cryptocurrencies
