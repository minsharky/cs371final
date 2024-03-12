# cs371final
The main.py file includes all the SPARQL queries used to get the university information from Wikidata and takes all the data into an RDF graph used for the reasoning.
The RDF graph is saved into graph_file.ttl file.
And all the reasoning was written in the reasoning.py file.

Instructions for use:

```bash
python3 main.py
```
After running the main.py file which should take around 30 seconds to a minute, run the reasoning.py file

```bash
python3 reasoning.py
```

The reasoning file should take 10-20 seconds to run and should output the filtered university URI's
