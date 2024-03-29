from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Literal, XSD

# Categorize admission rates
def categorize_admission_rate_and_label(subject, predicate, rate, g):
    label = ''
    if rate < 0.10:
        label = Literal('far reach')
    elif rate < 0.2:
        label = Literal('reach')
    elif rate < 0.4:
        label = Literal('target')
    else:
        label = Literal('safety')

    g.add((subject, predicate, label))

# Categorize student counts
def categorize_student_count_and_label(subject, predicate, rate, g):
    label = ''
    if rate < 1000:
        label = Literal('Small')
    elif rate < 30000:
        label = Literal('Medium')
    else:
        label = Literal('Large')

    g.add((subject, predicate, label))

# Create an RDF graph
g = Graph()
idealUniversityGraph = Graph()

# Set up the SPARQL endpoint URL
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

# SPARQL Query for all attributes
sparql.setQuery("""
    SELECT 
        ?university 
        ?universityLabel 
        ?universityTypeLabel
        (SAMPLE(?languageValue) AS ?language) 
        (SAMPLE(?locationValue) AS ?location) 
        (SAMPLE(?studentCountValue) AS ?studentCount) 
        (SAMPLE(?admissionRateValue) AS ?admissionRate) 
        (SAMPLE(?foundedValue) AS ?founded) 
        (SAMPLE(?memberOfValue) AS ?memberOf) 
        (SAMPLE(?calendarValue) AS ?calendar) 
    WHERE {
    {
        ?university wdt:P31 wd:Q875538;  # Public universities
        BIND("Public" AS ?universityTypeLabel)
    } UNION {
        ?university wdt:P31 wd:Q62078547;  # Public Research
        BIND("Public" AS ?universityTypeLabel)
    } UNION {
        ?university wdt:P31 wd:Q902104;  # Private universities
        BIND("Private" AS ?universityTypeLabel)
    } UNION {
        ?university wdt:P31 wd:Q23002054;  # Private not-for-profit universities
        BIND("Private" AS ?universityTypeLabel)
    }
    ?university wdt:P17 wd:Q30.        # Located in the United States
    OPTIONAL { ?university wdt:P2936 ?languageValue. }
    OPTIONAL { ?university wdt:P159 ?locationValue. }
    OPTIONAL { ?university wdt:P2196 ?studentCountValue. }
    OPTIONAL { ?university wdt:P5822 ?admissionRateValue. }
    OPTIONAL { ?university wdt:P571 ?foundedValue. }
    OPTIONAL { ?university wdt:P463 ?memberOfValue. }
    OPTIONAL { ?university wdt:P10588 ?calendarValue. }
    
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    GROUP BY ?university ?universityLabel ?universityTypeLabel
""")

# Specify the format of the results
sparql.setReturnFormat(JSON)

# Execute the query and retrieve the results
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    subject_uri = URIRef(result["university"]["value"])

    # Process each attribute with a check for existence
    attributes = ["universityTypeLabel", "language", "location", "studentCount", "admissionRate", "founded", "memberOf", "calendar"]
    for attr in attributes:
        if attr in result:
            predicate_uri = Literal(attr)
            object_uri = None
            # Check if the attribute is universityTypeLabel
            if attr == "universityTypeLabel":
                object_uri = Literal(result[attr]["value"])  # Store as a literal string
            elif attr == "studentCount":
                count = result[attr]["value"]
                # Label Student Count
                categorize_student_count_and_label(subject_uri, Literal('studentCountLevel'), int(count), g)
                object_uri = Literal(result[attr]["value"], datatype=XSD.integer)  # Store as a literal integer
            elif attr == "admissionRate":
                rate = result[attr]["value"]
                # Label the admission rate
                categorize_admission_rate_and_label(subject_uri, Literal('admissionRateLabel'), float(rate), g)
                object_uri = Literal(result[attr]["value"],  datatype=XSD.decimal)  # Store as a literal decimal
            elif attr == "founded":
                object_uri = Literal(result[attr]["value"],  datatype=XSD.dateTime)  # Store as a literal dateTime
            else:
                object_uri = URIRef(result[attr]["value"])
            g.add((subject_uri, predicate_uri, object_uri))

# File path for storing the graph
file_path = "./graph_file.ttl"

# Serialize and save the graph
with open(file_path, "wb") as f:
    g.serialize(f, format="turtle")