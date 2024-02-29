from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import XSD

# File path to the stored graph
file_path = "./graph_file.ttl"

# Create a new graph instance
g = Graph()
graph = Graph()

# Parse the graph from the file
g.parse(file_path, format="turtle")
graph.parse(file_path, format="turtle")

q0 = prepareQuery("""
    SELECT ?predicate ?value
    WHERE {
        ?university ?predicate ?value.
        FILTER(?university = <http://www.wikidata.org/entity/Q7988285>)
    }
""", initNs={"xsd": XSD})

member, admission, location, language, student, calendar, type, found = None, None, None, None, None, None, None, None

for row in graph.query(q0):
    pred = str(row.predicate)
    if(pred == "memberOf"):
        member = row.value.n3()
    if(pred == "admissionRate"):
        admission = row.value
    if(pred == "location"):
        location = row.value.n3()
    if(pred == "language"):
        language = (row.value).n3()
    if(pred == "studentCount"):
        student = row.value
    if(pred == "calendar"):
        calendar = row.value.n3()
    if(pred == "universityTypeLabel"):
        type = str(row.value)
    if(pred == "founded"):
        found = row.value
        start_year = int(found[:4]) - 50
        end_year = int(found[:4]) + 50

q1 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate1 ?universityType .
        FILTER(?predicate1 = "universityTypeLabel")
        {'FILTER(?universityType = "' + type + '")' if type is not None else ''}
    }}
""", initNs={"xsd": XSD})

q2 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate2 ?language .
        FILTER(?predicate2 = "language")
        {'FILTER(?language = "' + language + '")' if language is not None else ''}
    }}
""", initNs={"xsd": XSD})

q3 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        # Students count: 20,000 - 30,000
        ?university ?predicate3 ?studentCount .
        FILTER(?predicate3 = "studentCount")
        FILTER (datatype(?studentCount) = xsd:integer)
        FILTER(?studentCount >= 20000 && ?studentCount <= 30000)
    }
""", initNs={"xsd": XSD})

q4 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate4 ?admissionRate .
        FILTER(?predicate4 = "admissionRate")
        FILTER (datatype(?admissionRate) = xsd:decimal)
        FILTER(?admissionRate >= 0.06 && ?admissionRate <= 0.15)
    }}
""", initNs={"xsd": XSD})

q5 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate5 ?memberOf .
        FILTER(?predicate5 = "memberOf")
        {'FILTER(?memberOf = "' + member + '")' if member is not None else ''}
    }}
""", initNs={"xsd": XSD})

q6 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate6 ?founded .
        FILTER(?predicate6 = "founded")
        BIND(year(xsd:dateTime(?founded)) AS ?year)
        FILTER(?year >= {start_year} && ?year <= {end_year})
        }}
""", initNs={"xsd": XSD})

q7 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate7 ?location .
        FILTER(?predicate7 = "location")
        {'FILTER(?location = "' + location + '")' if location is not None else ''}
    }}
""", initNs={"xsd": XSD})

q8 = prepareQuery(f"""
    SELECT DISTINCT ?university
    WHERE {{
        ?university ?predicate7 ?calendar .
        FILTER(?predicate7 = "calendar")
        {"FILTER(?calendar = " + calendar + ")" if calendar is not None else ""}
    }}
""", initNs={"xsd": XSD})


filteredUniversities = set()

for row in g.query(q1):
    filteredUniversities.add(row.university)

q = [[q2, language], [q3, student], [q4, admission], [q5, member],  [q7, location], [q8, calendar]]

for tempQ, tempV in q:
    tempSet = set()
    if(tempV is not None):
        for row in g.query(tempQ):
            if row.university in filteredUniversities:
                tempSet.add(row.university)
        if(len(tempSet) != 0):
            filteredUniversities = tempSet

for uni in filteredUniversities:
    print(f"University that meet the criteria: {uni}")
