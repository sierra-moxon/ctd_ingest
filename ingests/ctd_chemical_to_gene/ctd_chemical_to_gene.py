import uuid

from koza.cli_runner import koza_app

source_name = "ctd_chemical_to_gene"

row = koza_app.get_row(source_name)


if row['InteractionActions'] == 'decreases^expression':

    chemical = {
        "id": 'MESH:' + row['ChemicalID'],
        "name": row['ChemicalName'],
        "source": 'infores:ctd'
    }

    gene = {"id": 'NCBIGene:' + row['GeneID'],
            "name": row['GeneSymbol'],
            "in_taxon": row['OrganismID'],
            "source": "infores:ctd"}

    predicate = "biolink:affects"
    object_aspect = "expression"
    object_direction = "decrease"

    association = {
        "id": "uuid:" + str(uuid.uuid1()),
        "subject": chemical.get("id"),
        "predicate": predicate,
        "object": "NCBIGene:"+gene.get("id"),
        "object_aspect": object_aspect,
        "object_direction": object_direction,
        "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
        "source": "infores:ctd"
    }
    print(row)
    print(association)
    koza_app.writer.write_node(chemical)
    koza_app.writer.write_node(gene)
    koza_app.writer.write_edge(association)
