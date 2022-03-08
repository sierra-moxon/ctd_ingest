Toy repository to try out several biolink-model predicate refactoring methods
Will generate KGX formatted files

For local development:

```sh
poetry install
poetry run koza transform --source chemical_to_disease.yaml --output-format tsv
```

Next:
load to neo4j
spin up a TRAPI endpoint