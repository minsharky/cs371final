from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS

# Create an RDF graph
g = Graph()

# Set up the SPARQL endpoint URL
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

# Language Used
sparql.setQuery("""
    SELECT ?university ?universityLabel ?language ?languageLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P2936 ?language.      # City of the university
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
# Language Used
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('http://www.wikidata.org/prop/direct/P2936')
    object_uri = URIRef("http://www.wikidata.org/entity/"+result["language"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

for triple in g:
    print(triple)