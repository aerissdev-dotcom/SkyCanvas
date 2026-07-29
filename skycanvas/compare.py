from skycanvas.render import get_constellation_lines
from skycanvas.tonight import get_visible_constellations
from skycanvas.constellations import CONSTELLATIONS
from rich import print
from rich.text import Text


def print_compare(first, second):

    first_lines = get_constellation_lines(first)
    second_lines = get_constellation_lines(second)

    print(
        f"\n[bold cyan]{first.title()}[/bold cyan]"
        f"{' ' * 25}"
        f"[bold red]VS[/bold red]"
        f"{' ' * 25}"
        f"[bold magenta]{second.title()}[/bold magenta]\n"
    )


    for i in range(max(len(first_lines), len(second_lines))):

        left = first_lines[i] if i < len(first_lines) else ""
        right = second_lines[i] if i < len(second_lines) else ""


        line = Text()

        line.append(
            left.ljust(55)
        )

        line.append(
            right
        )


        line.highlight_regex(
            r"\*",
            style="bold yellow"
        )


        print(line)



def compare_constellations(first, second):

    first = first.lower()
    second = second.lower()


    if first != "tonight" and first not in CONSTELLATIONS:
        print(f"Unknown constellation: {first}")
        return


    if second != "tonight" and second not in CONSTELLATIONS:
        print(f"Unknown constellation: {second}")
        return


    first_list = (
        get_visible_constellations()
        if first == "tonight"
        else [first]
    )


    second_list = (
        get_visible_constellations()
        if second == "tonight"
        else [second]
    )


    for left in first_list:

        for right in second_list:

            print_compare(
                left,
                right
            )

            print("\n")