from SPARQLWrapper import SPARQLWrapper, JSON

# Set up the SPARQL endpoint URL
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

# Define the SPARQL query
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE {
        <http://dbpedia.org/resource/Python_(programming_language)> rdfs:label ?label .
        FILTER (langMatches(lang(?label), "en"))
    }
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

# Process the results
for result in results["results"]["bindings"]:
    print(result["universityLabel"]["value"])
