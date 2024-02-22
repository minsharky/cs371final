from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS

# Create an RDF graph
g = Graph()
idealUniversityGraph = Graph()

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
    subject_uri = URIRef(result["universityLabel"]["value"])
    predicate_uri = URIRef('language used')
    object_uri = URIRef(result["languageLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# private/public university
# Private University
sparql.setQuery("""
SELECT ?universityLabel
WHERE {
  ?university 
      wdt:P31 wd:Q902104;  
      wdt:P17 wd:Q30.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["universityLabel"]["value"])
    predicate_uri = URIRef('typeOfInstitution')
    object_uri = URIRef('Private University')
    g.add((subject_uri, predicate_uri, object_uri))

#Public University
sparql.setQuery("""
SELECT ?universityLabel
WHERE {
  ?university 
      wdt:P31 wd:Q875538; 
      wdt:P17 wd:Q30.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["universityLabel"]["value"])
    predicate_uri = URIRef('typeOfInstitution')
    object_uri = URIRef('Public University')
    g.add((subject_uri, predicate_uri, object_uri))

for subject, predicate, obj in g:
    # Process the triple
    print("University:", subject)
    print("Predicate:", predicate)
    print("Object:", obj)
    print()   