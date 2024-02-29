from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import XSD

# File path to the stored graph
file_path = "./graph_file.ttl"

# Create a new graph instance
g = Graph()

# Parse the graph from the file
g.parse(file_path, format="turtle")

# for subject, predicate, obj in g:
#     print("University:", subject)
#     print("Predicate:", predicate)
#     print("Object:", obj)
#     print()

q1 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        ?university ?predicate1 ?universityType .
        FILTER(?predicate1 = "universityTypeLabel")
        FILTER(?universityType = "Private")
    }
""", initNs={"xsd": XSD})

q2 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        ?university ?predicate2 ?language .
        FILTER(?predicate2 = "language")
        FILTER(?language = <http://www.wikidata.org/entity/Q1860>)
    }
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

q4 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        ?university ?predicate4 ?admissionRate .
        FILTER(?predicate4 = "admissionRate")
        FILTER (datatype(?admissionRate) = xsd:decimal)
        FILTER(?admissionRate >= 0.06 && ?admissionRate <= 0.15)
    }
""", initNs={"xsd": XSD})

q5 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        ?university ?predicate5 ?memberOf .
        FILTER(?predicate5 = "memberOf")
        FILTER(?memberOf = <http://www.wikidata.org/entity/Q49113>)
    }
""", initNs={"xsd": XSD})

q6 = prepareQuery("""
    SELECT DISTINCT ?university
    WHERE {
        ?university ?predicate6 ?founded .
        FILTER(?predicate6 = "founded")
        BIND(year(xsd:dateTime(?founded)) AS ?year)
        FILTER(?year >= 1850 && ?year <= 1900)
    }
""", initNs={"xsd": XSD})

filteredUniversities = set()

for row in g.query(q1):
    filteredUniversities.add(row.university)

q = [q2, q3, q4, q5, q6]

for tempQ in q:
    tempSet = set()
    for row in g.query(tempQ):
        if row.university in filteredUniversities:
            tempSet.add(row.university)
    filteredUniversities = tempSet

for uni in filteredUniversities:
    print(f"University that meet the criteria: {uni}")
