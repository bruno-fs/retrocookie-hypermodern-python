"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Retrocookie Hypermodern Python."""


if __name__ == "__main__":
    main(prog_name="retrocookie-hypermodern-python")  # pragma: no cover
