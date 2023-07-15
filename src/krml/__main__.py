"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """krml."""


if __name__ == "__main__":
    main(prog_name="krml")  # pragma: no cover
