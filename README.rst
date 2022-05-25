Toy repository to try out several biolink-model predicate refactoring methods
Will generate KGX formatted files

prereqs:

- must have ingest.py in two level deep directory (here: ingests/name_of_ingest)
- download and decompress manually
- make sure name in source.yaml matches name of py file and yaml file

For local development:

```sh
poetry install
poetry run koza transform --source ingests/ctd_chemical_to_gene/ctd_chemical_to_gene.yaml --output-format tsv
```

```sh
poetry install
poetry run python ctd_ingest/main.py transform --help
```


Next:
load to neo4j with kgx
spin up a TRAPI endpoint with plater

