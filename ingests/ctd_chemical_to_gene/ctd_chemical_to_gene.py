import uuid

from koza.cli_runner import koza_app

source_name = "ctd_chemical_to_gene"

row = koza_app.get_row(source_name)


interaction_actions = [a for a in row['InteractionActions'].split("|")]
# ['decreases^expression','increases^abundance']

for action in interaction_actions:
    qualified_action = action.split("^")
    if qualified_action[1] == 'cotreatment' or qualified_action[1] == 'response to substance':
        pass
    aspect = qualified_action[1]
    direction = qualified_action[0]

    chemical = {
        "id": 'MESH:' + row['ChemicalID'],
        "name": row['ChemicalName'],
        "source": 'infores:ctd'
    }

    gene = {"id": row['GeneID'],
            "name": row['GeneSymbol'],
            "in_taxon": row['OrganismID'],
            "source": "infores:ctd"}

    predicate = "biolink:affects"
    object_aspect = aspect
    object_direction = direction

    if object_direction == 'affects':
        association = {
            "id": "uuid:" + str(uuid.uuid1()),
            "subject": chemical.get("id"),
            "predicate": predicate,
            "object": gene.get("id"),
            "object_aspect": object_aspect,
            "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
            "source": "infores:ctd"
        }
    else:
        association = {
            "id": "uuid:" + str(uuid.uuid1()),
            "subject": chemical.get("id"),
            "predicate": predicate,
            "object": gene.get("id"),
            "object_aspect": object_aspect,
            "object_direction": object_direction,
            "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
            "source": "infores:ctd"
        }
    koza_app.writer.write_node(chemical)
    koza_app.writer.write_node(gene)
    koza_app.writer.write_edge(association)
