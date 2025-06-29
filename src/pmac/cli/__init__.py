"""Typer-powered CLI for PMAC Core."""
from __future__ import annotations

from pathlib import Path

import typer

from pmac import __version__
from pmac.validators import validate

app = typer.Typer(add_help_option=True, no_args_is_help=True, rich_help_panel="Commands")


@app.callback()
def _root(ctx: typer.Context, version: bool = typer.Option(False, "--version", "-v", help="Show PMAC version and exit")) -> None:
    """Project‑Management‑As‑Code command‑line interface."""
    if version:
        typer.echo(f"PMAC Core v{__version__}")
        raise typer.Exit()


@app.command(name="validate", help="Validate a PMAC JSON file against the bundled schema.")
def validate_cmd(file: Path = typer.Argument(..., exists=True, readable=True, help="Path to pmac.json file")) -> None:
    ok, errors = validate(file)
    if ok:
        typer.secho("Validation successful ✅", fg=typer.colors.GREEN)
        raise typer.Exit(code=0)
    for err in errors:
        typer.echo(f"❌ {err}")
    raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
