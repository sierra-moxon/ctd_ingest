import uuid

from koza.cli_runner import koza_app

source_name = "ctd_chemical_to_disease"

row = koza_app.get_row(source_name)

if row['DirectEvidence'] in ['marker/mechanism', 'therapeutic']:

    chemical = {
        "id": 'MESH:' + row['ChemicalID'],
        "name": row['ChemicalName'],
        "source": 'infores:ctd'
    }

    disease = {"id": row['DiseaseID'],
               "name": row['DiseaseID'],
               "source": "infores:ctd"}

    if row['DirectEvidence'] == 'marker/mechanism':
        predicate = "biolink:biomarker_for"
        relation = "RO:0002607"
    elif row['DirectEvidence'] == 'therapeutic':
        predicate = "treats"
        relation = "RO:0002606"

    association = {
        "id": "uuid:" + str(uuid.uuid1()),
        "subject": chemical.get("id"),
        "predicate": predicate,
        "object": disease.get("id"),
        "relation": relation,
        "publications": ["PMID:" + p for p in row['PubMedIDs'].split("|")],
        "source": "infores:ctd"
    }
    koza_app.writer.write_node(chemical)
    koza_app.writer.write(disease)
    koza_app.writer.write_edge(association)
