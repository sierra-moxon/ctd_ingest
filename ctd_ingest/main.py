import typer
from cat_merge.merge import merge

typer_app = typer.Typer()
OUTPUT_DIR = "output"


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
    merge_files(input_dir=input_dir, output_dir=output_dir)


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


if __name__ == "__main__":
    typer_app()
