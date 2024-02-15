from SPARQLWrapper import SPARQLWrapper, JSON

# Set up the SPARQL endpoint URL
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

# Define the SPARQL query
sparql.setQuery("""
    SELECT ?cityLabel WHERE {
    ?university wdt:P31 wd:Q615150, wd:Q902104;
    wdt:P131 ?city.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
LIMIT 1
""")

# Specify the format of the results (optional)
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the results
for result in results["results"]["bindings"]:
    print(result["label"]["value"])
