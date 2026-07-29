from datetime import datetime

from rich import print
from rich.table import Table

from skycanvas.constellations import CONSTELLATIONS
from skycanvas.render import render_constellation

def get_current_month():

    return datetime.now().strftime("%B")


def get_visible_constellations():

    current_month = get_current_month()

    visible = []

    for key, constellation in CONSTELLATIONS.items():

        months = constellation["best_visible_months"]

        if current_month in months:
            visible.append(key)

    return visible


def show_tonight():

    visible = get_visible_constellations()

    if not visible:
        print("[bold red]No constellation data available.[/bold red]")
        return


    table = Table(
        title="[bold cyan]Visible Tonight[/bold cyan]",
        title_justify="left",
        show_lines=True,
        border_style="cyan"
    )

    table.add_column("Name", vertical="middle")
    table.add_column("Common Name", vertical="middle")
    table.add_column("Brightest Star", vertical="middle")
    table.add_column("Best Visible Months", vertical="middle")


    for constellation in visible:

        data = CONSTELLATIONS[constellation]

        table.add_row(
            data["name"],
            data["common_name"],
            data["brightest_star"],
            ", ".join(data["best_visible_months"])
        )


    print(table)

    print("\n[bold yellow]Constellations:[/bold yellow]\n")

    for constellation in visible:
        data = CONSTELLATIONS[constellation]

        print(f"[bold cyan]{data['name']}[/bold cyan] - {data['common_name']}\n")
        render_constellation(constellation)
        print ("\n")