from koza.cli_runner import transform_source
from koza.model.config.source_config import OutputFormat
from cat_merge.merge import merge

OUTPUT_DIR = "output"


def transform_one(
        ingest: str,
        output_dir: str = OUTPUT_DIR,
):
    transform_source(
        source=ingest,
        output_dir=f"{output_dir}/transform_output",
        output_format=OutputFormat.tsv,
        local_table=None,
        global_table=None
    )


def transform_all(
        ingest: str,
        output_dir: str = OUTPUT_DIR
):

    try:
        transform_one(
            ingest=ingest,
            output_dir=output_dir,
        )
    except Exception as e:
        print(e)


def merge_files(
    name: str = "ctd_pre_neo",
    input_dir: str = f"{OUTPUT_DIR}/transform_output",
    output_dir: str = OUTPUT_DIR,
):
    merge(
        name=name,
        input_dir=input_dir,
        output_dir=output_dir
    )
