import typer
from pathlib import Path
from pmac import __version__
from pmac.validators import validate

app = typer.Typer(add_help_option=True, no_args_is_help=True)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, version: bool = typer.Option(False, "--version", "-v")):
    """Project-Management-As-Code CLI (legacy stub)."""
    if version:
        typer.echo(f"PMAC Core v{__version__}")
        raise typer.Exit()

@app.command()
def validate_cmd(file: Path):
    """Validate a PMAC JSON file."""
    ok, errors = validate(file)
    if ok:
        typer.secho("Validation successful ✅", fg=typer.colors.GREEN)
    else:
        for e in errors:
            typer.echo(f"❌ {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
