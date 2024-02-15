from SPARQLWrapper import SPARQLWrapper, JSON

# Set up the SPARQL endpoint URL
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

# Define the SPARQL query
sparql.setQuery("""
    SELECT ?universityLabel
WHERE {
  ?university 
      wdt:P31 wd:Q3918;  # Instances of all universities
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()
for r 
print(results.keys)
# Process the results
# for result in results["results"]["bindings"]:
#     print(result["universityLabel"]["value"])
