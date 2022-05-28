import typer
import cli_utils

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
    cli_utils.merge_files(input_dir=input_dir, output_dir=output_dir)


if __name__ == "__main__":
    typer_app()
