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
      wdt:P2936 ?language.      
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

# Location (city)
sparql.setQuery("""
    SELECT ?university ?universityLabel ?location ?locationLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P159 ?location.      # City of the university
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
    predicate_uri = URIRef('location')
    object_uri = URIRef(result["locationLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Student count
sparql.setQuery("""
    SELECT ?university ?universityLabel ?studentCount ?studentCountLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P2196 ?studentCount.      # City of the university
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
    predicate_uri = URIRef('studentCount')
    object_uri = URIRef(result["studentCountLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))




# Admission Rate
sparql.setQuery("""
    SELECT ?university ?universityLabel ?admissionRate ?admissionRateLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P5822 ?admissionRate.      # City of the university
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
    predicate_uri = URIRef('admissionRate')
    object_uri = URIRef(result["admissionRateLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))


# Founded
sparql.setQuery("""
    SELECT ?university ?universityLabel ?founded ?foundedLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P571 ?founded.      # City of the university
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
    predicate_uri = URIRef('founded')
    object_uri = URIRef(result["foundedLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Member of (ivy league etc.)
sparql.setQuery("""
    SELECT ?university ?universityLabel ?memberOf ?memberOfLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P463 ?memberOf.      # City of the university
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
    predicate_uri = URIRef('memberOf')
    object_uri = URIRef(result["memberOfLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))



# academic calendar type
sparql.setQuery("""
    SELECT ?university ?universityLabel ?calendar ?calendarLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P10588 ?calendar.      # City of the university
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
    predicate_uri = URIRef('calendar')
    object_uri = URIRef(result["calendarLabel"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))




# print out
for subject, predicate, obj in g:
    # Process the triple
    print("University:", subject)
    print("Predicate:", predicate)
    print("Object:", obj)
    print()
