import typer
from rich import print
from skycanvas.logo import show_logo

app = typer.Typer(name="skycanvas", help="ASCII constellation viewer powered by astronomical data.")

# Commands:

# - skycanvas version, skycanvas -v, skycanvas --version
# - skycanvas list
# - skycanvas compare [Constellation 1 / tonight] vs [Constellation 2 / tonight]
# - skycanvas tonight
# - skycanvas location [city]
# - skycanvas --export [constellation / tonight] png / jpg / svg / bmp
# - skycanvas logo 
# - skycanvas --help
# - skycanvas man
# - skycanvas random
# - skycanvas [Constallation]

@app.command()
def list():
    """Show the list of constellations"""
    print("TODO")


@app.command()
def version():
    """Show SkyCanvas version"""
    print("[bold cyan]SkyCanvas v0.1.0[/bold cyan]")

@app.command()
def logo():
    """Show SkyCanvas logo"""
show_logo()

if __name__ == "__main__":
    app()