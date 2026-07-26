import typer
from rich import print
from rich.columns import Columns
from rich.table import Table
from skycanvas.logo import show_logo
from skycanvas.constellations import CONSTELLATIONS
import random

list_of_constellations = ["orion", "ursa_major", "cassiopeia", "scorpius", "taurus", "gemini",  "leo", "cygnus", "lyra", "aquila", "pegasus", "andromeda", "canis_major", "canis_minor", "draco", "sagittarius", "virgo", "aries", "capricornus", "pisces", "ursa_minor", "perseus", "cepheus", "hydra", "centaurus", "crux", "phoenix", "libra", "aquarius", "cancer"]

app = typer.Typer(name="skycanvas", help="ASCII constellation viewer powered by astronomical data.")

# Commands:

# - skycanvas version, skycanvas -v, skycanvas --version
# - skycanvas list
# - skycanvas compare [Constellation 1 / tonight] vs [Constellation 2 / tonight]
# - skycanvas tonight
# - skycanvas location [city]
# - skycanvas --export [constellation / tonight] png / jpg / svg / bmp
# - skycanvas logo [DONE]
# - skycanvas --help [DONE]
# - skycanvas man
# - skycanvas rand
# - skycanvas [Constallation]


@app.command()
def list():
    """Show the list of constellations"""
    table = Table(
        title="[bold yellow]Available constellations to view:[/bold yellow]\n", 
        title_justify="left",
        show_header=False, 
        box=None,
        show_lines=True 
    )
    
    table.add_column("Col 1", width=25)
    table.add_column("Col 2")

    for i in range(0, len(list_of_constellations), 2):
        chunk = list_of_constellations[i:i+2]
        if len(chunk) == 2:
            table.add_row(*chunk)
        else:
            table.add_row(chunk[0], "")

    print(table)

@app.command()
def version():
    """Show SkyCanvas version"""
    print("[bold cyan]SkyCanvas v0.1.0[/bold cyan]")

@app.command()
def logo():
    """Show SkyCanvas logo"""
    show_logo()

@app.command()
def rand():
    """Show random constellation"""
    randIndex = list_of_constellations[random.randint(0, 29)]

    for i in (CONSTELLATIONS[randIndex]["best_visible_months"]):
        best_visible_months = ", ".join(CONSTELLATIONS[randIndex]["best_visible_months"])

    for i in (CONSTELLATIONS[randIndex]["stars"]):
            stars = ", ".join(CONSTELLATIONS[randIndex]["stars"])

    connections_list = CONSTELLATIONS[randIndex]["connections"]
    formatted_connections = "\n".join(" -> ".join(pair) for pair in connections_list)

    table = Table(
        title="[bold cyan]Random Constellation[/bold cyan]",
        title_justify="left",
        show_lines=True,
        border_style="cyan"
    )

    table.add_column("Name", vertical="middle")
    table.add_column("Common Name", vertical="middle")
    table.add_column("Best Visible Months", vertical="middle")
    table.add_column("Brightest Star", vertical="middle")
    table.add_column("Stars", vertical="middle")
    table.add_column("Connections", vertical="middle")


    table.add_row(CONSTELLATIONS[randIndex]["name"], CONSTELLATIONS[randIndex]["common_name"], best_visible_months, CONSTELLATIONS[randIndex]["brightest_star"], stars, formatted_connections)
    print(table)

if __name__ == "__main__":
    app()