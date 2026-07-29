import typer
from rich import print
from rich.columns import Columns
from rich.table import Table
from skycanvas.logo import show_logo
from skycanvas.constellations import CONSTELLATIONS
from skycanvas.tonight import show_tonight
from skycanvas.render import render_constellation
from skycanvas.compare import compare_constellations
import random



list_of_constellations = ["orion", "ursa_major", "cassiopeia", "scorpius", "taurus", "gemini",  "leo", "cygnus", "lyra", "aquila", "pegasus", "andromeda", "canis_major", "canis_minor", "draco", "sagittarius", "virgo", "aries", "capricornus", "pisces", "ursa_minor", "perseus", "cepheus", "hydra", "centaurus", "crux", "phoenix", "libra", "aquarius", "cancer"]

app = typer.Typer(name="skycanvas", help="ASCII constellation viewer powered by astronomical data.")

# Commands:

# - skycanvas version, skycanvas -v, skycanvas --version [DONE]
# - skycanvas list [DONE]
# - skycanvas compare [Constellation 1 / tonight] vs [Constellation 2 / tonight]
# - skycanvas tonight
# - skycanvas location [city]
# - skycanvas --export [constellation / tonight] png / jpg / svg / bmp
# - skycanvas logo [DONE]
# - skycanvas --help [DONE]
# - skycanvas man [DONE]
# - skycanvas rand [DONE]
# - skycanvas constellation [Constallation] [DONE]


def version_callback(value: bool):
    if value:
        print("SkyCanvas v0.1.0")
        raise typer.Exit()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, version: bool = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True, help="Show SkyCanvas version.")):
    if ctx.invoked_subcommand is None:
        show_logo()
        print("\nRun 'skycanvas --help' to see available commands.")
        raise typer.Exit()

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

    print("\n")
    print(f"[bold cyan]{randIndex}[/bold cyan]")
    render_constellation(randIndex)

@app.command()
def man():
    """Show the SkyCanvas manual."""
    show_logo()

    print("""
[bold cyan]SkyCanvas Manual[/bold cyan]


[bold red]NAME[/bold red]

[bold yellow]SkyCanvas[/bold yellow] - ASCII constellation viewer powered by astronomical data.

[bold red]USAGE[/bold red]

  [bold yellow]skycanvas[/bold yellow] [COMMAND]
          

[bold red]COMMANDS[/bold red]

  [bold cyan]version[/bold cyan]       Show SkyCanvas version.

  [bold cyan]man[/bold cyan]           Show SkyCanvas manual.

  [bold cyan]compare[/bold cyan]       Compare two different constellations.

  [bold cyan]tonight[/bold cyan]       Show today's stars alignment in your city.

  [bold cyan]list[/bold cyan]          Display the list of available constellations.

  [bold cyan]--export[/bold cyan]      Export the constellation or the view of tonight's stars to an image form.

  [bold cyan]rand[/bold cyan]          Show random constellation and its data.

  [bold cyan]--help[/bold cyan]        Show command help.
          
  [bold cyan]constellation[/bold cyan] Show a constellation of choice.

  [bold cyan]logo[/bold cyan]          Show a logo of SkyCanvas.

  [bold cyan]location[/bold cyan]      Establish a city you live in (only for stars alignment statistics)

[bold red]AUTHOR[/bold red]

  aeriss-dev


[bold red]GITHUB[/bold red]

  [link=https://github.com/aerissdev-dotcom]github.com/aerissdev-dotcom[/link]


[bold red]LICENSE[/bold red]

  MIT License


[bold red]VERSION[/bold red]

  0.1.0
""")

@app.command()
def test_render():
    """Test constellation renderer"""
    render_constellation("aries")

@app.command()
def constellation(name: str):
    """Show selected constellation"""

    name = name.lower()

    if name not in CONSTELLATIONS:
        print(f"Unknown constellation: {name}")
        return

    best_visible_months = ", ".join(
        CONSTELLATIONS[name]["best_visible_months"]
    )

    stars = ", ".join(
        CONSTELLATIONS[name]["stars"]
    )

    connections_list = CONSTELLATIONS[name]["connections"]

    formatted_connections = "\n".join(
        " -> ".join(pair)
        for pair in connections_list
    )


    table = Table(
        title="[bold cyan]Constellation Information[/bold cyan]",
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


    table.add_row(
        CONSTELLATIONS[name]["name"],
        CONSTELLATIONS[name]["common_name"],
        best_visible_months,
        CONSTELLATIONS[name]["brightest_star"],
        stars,
        formatted_connections
    )


    print(table)

    print("\n")

    render_constellation(name)

@app.command()
def tonight():
    """Show visible constellations tonight."""
    show_tonight()

@app.command()
def compare(first:str, second:str):
    """Compare two constellations or tonight's visible constellations."""
    compare_constellations(first, second)

if __name__ == "__main__":
    app()