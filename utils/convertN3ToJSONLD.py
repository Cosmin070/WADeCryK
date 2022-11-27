from rdflib import Graph, plugin
from rdflib.serializer import Serializer

g = Graph()
g.parse("cryptocurrency.nt", format="nt")

# f = open("cryptocurrency.jsonld", "w")
# f.write(g.serialize(format='json-ld', indent=4))
g.serialize(format='json-ld', indent=4, destination="cryptocurrency.jsonld")