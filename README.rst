Toy repository to try out several biolink-model predicate refactoring methods
Will generate KGX formatted files

prereqs:

- must have ingest.py in two level deep directory (here: ingests/name_of_ingest)
- download and decompress manually
- make sure name in source.yaml matches name of py file and yaml file

For local development:

transform CTD csv to KGX format:
```sh
poetry install
poetry run koza transform --source ingests/ctd_chemical_to_gene/ctd_chemical_to_gene.yaml --output-format tsv
```

remove duplicate nodes? - results in some weird top level rows:
```sh
poetry install
poetry run python ctd_ingest/main.py merge --input-dir output --output-dir output/merged
```

load to neo4j with kgx:
```sh
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/s3cr3t neo4j
poetry run python ctd_ingest/load_neo.py --nodes output/ctd_chemical_to_gene_nodes.tsv --edges output/ctd_chemical_to_gene_edges.tsv --uri bolt://localhost:7687
```


Next:
spin up a TRAPI endpoint with plater

