# Project Name: University Recommender

## Team Members
- Yash Agrawal
- Minseo Kim
- Wei Sun
- Karen Lee

## Project Overview

The University Recommender system aims to provide prospective college students with university recommendations that are "similar" to a university of their interest. By inputting a university name, users can discover alternative schools that match based on various attributes. This project leverages data from Wikidata and utilizes RDF (Resource Description Framework) graphs for data representation and SPARQL for data querying and reasoning.

## Goal of the Project

To create a program that recommends universities similar to a given input university based on a list of attributes, thereby assisting prospective students in exploring universities similar to those they are already interested in.

## What We Did

- **Data Querying:** Utilized SPARQL to query Wikidata for university data based on selected attributes.
- **Data Representation:** Employed RDF graphs to store information about universities, including attributes like admission rates, student counts, and more.
- **Reasoning:** Developed a reasoning process to recommend universities by comparing the semantic attributes of the input university with those in the RDF graph.

## Getting Started

To use this project, you will need Python 3.x and the following Python libraries: rdflib and SPARQLWrapper. You can install these dependencies using pip:

```
pip install rdflib SPARQLWrapper
```
## Files Included

1. `graph_file.ttl`: Contains RDF data about universities.
2. `main.py`: Python script for querying Wikidata and generating the RDF graph.
3. `reasoning.py`: Python script for reasoning over the RDF graph to recommend similar universities.

## Strengths and Weaknesses

- **Strengths:** Utilization of Wikidata allowed for a rich set of university data. The creation of labels for university attributes like student count and admission rate enabled more nuanced comparisons.
- **Weaknesses:** The reasoning process's attribute order was predetermined, introducing potential biases. The variability in the completeness of university data in Wikidata might affect the accuracy of recommendations.

## Next Steps

- Enhance the complexity of attributes for better comparison.
- Explore alternative databases for more accurate data.
- Allow users to input a list of universities for recommendations to understand their preferences better.
- Expand the knowledge base to include international universities.

## Usage

1. Run `main.py` to update `graph_file.ttl` with the latest university data from Wikidata.
    ```
    python main.py
    ```
2. Execute `reasoning.py` to generate recommendations based on the input university.
    ```
    python reasoning.py
    ```

## Building Upon This Project

This project offers several avenues for extension and improvement, such as refining the attribute comparison mechanism, incorporating more comprehensive datasets, and expanding the system to accommodate user preferences more effectively.

