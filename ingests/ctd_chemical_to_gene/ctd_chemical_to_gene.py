import uuid

from koza.cli_runner import koza_app

source_name = "ctd_chemical_to_gene"

row = koza_app.get_row(source_name)


interaction_actions = [a for a in row['InteractionActions'].split("|")]
# ['decreases^expression','increases^abundance']

if len(interaction_actions) > 1:
    pass
else:
    for action in interaction_actions:
        qualified_action = action.split("^")
        object_aspect = qualified_action[1]
        if qualified_action[0] == "increases":
            object_direction = "increased"
        elif qualified_action[0] == "decreases":
            object_direction = "decreased"
        else:
            object_direction = qualified_action[0]

        chemical = {
            "id": 'MESH:' + row['ChemicalID'],
            "name": row['ChemicalName'],
            "source": 'infores:ctd',
            "category": "biolink:ChemicalEntity"
        }

        gene = {"id": "NCBIGene:" + row['GeneID'],
                "name": row['GeneSymbol'],
                "in_taxon": row['OrganismID'],
                "source": "infores:ctd",
                "category": "biolink:Gene"}

        if qualified_action[1] == 'cotreatment' or qualified_action[1] == 'response to substance':
            continue

        if qualified_action[1] == 'binding':
            predicate = "biolink:physically_interacts_with"

            association = {
                "id": "uuid:" + str(uuid.uuid1()),
                "subject": chemical.get("id"),
                "predicate": predicate,
                "object": gene.get("id"),
                "object_direction": object_direction,
                "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
                "source": "infores:ctd"
            }

            koza_app.writer.write_node(chemical)
            koza_app.writer.write_node(gene)
            koza_app.writer.write_edge(association)

            predicate = "biolink:affects"
            object_aspect = "activity"

            association = {
                "id": "uuid:" + str(uuid.uuid1()),
                "subject": chemical.get("id"),
                "predicate": predicate,
                "qualified_predicate": "causes",
                "object": gene.get("id"),
                "object_aspect": object_aspect,
                "object_direction": object_direction,
                "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
                "source": "infores:ctd"
            }

            koza_app.writer.write_node(chemical)
            koza_app.writer.write_node(gene)
            koza_app.writer.write_edge(association)

        else:
            if object_direction == 'affects':
                association = {
                    "id": "uuid:" + str(uuid.uuid1()),
                    "subject": chemical.get("id"),
                    "predicate": "affects",
                    "qualified_predicate": "causes",
                    "object": gene.get("id"),
                    "object_aspect": object_aspect,
                    "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
                    "source": "infores:ctd"
                }
            else:
                association = {
                    "id": "uuid:" + str(uuid.uuid1()),
                    "subject": chemical.get("id"),
                    "predicate": "affects",
                    "qualified_predicate": "causes",
                    "object": gene.get("id"),
                    "object_aspect": object_aspect,
                    "object_direction": object_direction,
                    "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
                    "source": "infores:ctd"
                }
            koza_app.writer.write_node(chemical)
            koza_app.writer.write_node(gene)
            koza_app.writer.write_edge(association)

