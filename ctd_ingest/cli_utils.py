from cat_merge.merge import merge

OUTPUT_DIR = "output"


def merge_files(
    name: str = "ct-ingest-test",
    input_dir: str = f"{OUTPUT_DIR}/transform_output",
    output_dir: str = OUTPUT_DIR,
):

    merge(
        name=name,
        input_dir=input_dir,
        output_dir=output_dir
    )