from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery

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
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('languageUsed')
    object_uri = URIRef(result["language"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# private/public university
# Private University
sparql.setQuery("""
    SELECT ?university
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
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('typeOfInstitution')
    object_uri = URIRef('http://www.wikidata.org/entity/Q902104')
    g.add((subject_uri, predicate_uri, object_uri))

#Public University
sparql.setQuery("""
    SELECT ?university
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
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('typeOfInstitution')
    object_uri = URIRef('http://www.wikidata.org/entity/Q875538')
    g.add((subject_uri, predicate_uri, object_uri))

# Location (city)
sparql.setQuery("""
    SELECT ?university ?universityLabel ?location ?locationLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P159 ?location.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()
# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('location')
    object_uri = URIRef(result["location"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Student count
sparql.setQuery("""
    SELECT ?university ?universityLabel ?studentCount ?studentCountLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P2196 ?studentCount. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('studentCount')
    object_uri = URIRef(result["studentCount"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Admission Rate
sparql.setQuery("""
    SELECT ?university ?universityLabel ?admissionRate ?admissionRateLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P5822 ?admissionRate. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('admissionRate')
    object_uri = URIRef(result["admissionRate"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))


# Founded
sparql.setQuery("""
    SELECT ?university ?universityLabel ?founded ?foundedLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P571 ?founded. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('founded')
    object_uri = URIRef(result["founded"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Member of (ivy league etc.)
sparql.setQuery("""
    SELECT ?university ?universityLabel ?memberOf ?memberOfLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P463 ?memberOf. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('memberOf')
    object_uri = URIRef(result["memberOf"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))


# academic calendar type
sparql.setQuery("""
    SELECT ?university ?universityLabel ?calendar ?calendarLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
      wdt:P17 wd:Q30;
      wdt:P10588 ?calendar.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the JSON results and convert them to RDF triples
for result in results["results"]["bindings"]:
    # Add RDF triples to the graph
    subject_uri = URIRef(result["university"]["value"])
    predicate_uri = URIRef('calendar')
    object_uri = URIRef(result["calendar"]["value"])
    g.add((subject_uri, predicate_uri, object_uri))

# Assuming the URI for American Sign Language is http://www.wikidata.org/entity/Q14759
ASL_URI = URIRef("http://www.wikidata.org/entity/Q14759")

# Prepare a SPARQL query to retrieve universities that use American Sign Language
q = prepareQuery("""
    SELECT ?university
    WHERE {
        ?university <languageUsed> ?language .
        FILTER(?language = <http://www.wikidata.org/entity/Q14759>)
    }
    """, initNs={"languageUsed": URIRef('languageUsed')})

# Execute the query on the graph
for row in g.query(q):
    # Each row is a tuple of RDF terms in the SELECT clause
    print(f"University using American Sign Language: {row.university}")

# print out
# for subject, predicate, obj in g:
#     # Process the triple
#     print("University:", subject)
#     print("Predicate:", predicate)
#     print("Object:", obj)
#     print()