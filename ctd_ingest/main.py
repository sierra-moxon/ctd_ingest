import typer
from ctd_ingest import cli_utils

typer_app = typer.Typer()
OUTPUT_DIR = "output"


@typer_app.command()
def transform(
        output_dir: str = typer.Option(OUTPUT_DIR, help="Directory to output data"),
        do_merge: bool = typer.Option(False, "--merge", help="Merge output dir after ingest"),
        ingest: str = typer.Option(False, help="path to ingest config yaml file"),
):
    """
    Something descriptive
    """
    cli_utils.transform_all(
        output_dir=output_dir,
        ingest=ingest
    )
    if do_merge:
        merge(f"{output_dir}/transform_output", output_dir)


@typer_app.command()
def merge(
        input_dir: str = typer.Option(
            f"{OUTPUT_DIR}/transform_output",
            help="Directory containing nodes and edges to be merged",
        ),
        output_dir: str = typer.Option(f"{OUTPUT_DIR}", help="Directory to output data"),
):
    """
    Something descriptive
    """
    cli_utils.merge_files(input_dir=input_dir, output_dir=output_dir)


if __name__ == "__main__":
    typer_app()
