from pathlib import Path
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from rich import print
from skycanvas.render import get_constellation_lines
from skycanvas.tonight import get_visible_constellations
from skycanvas.constellations import CONSTELLATIONS

EXPORT_DIR = Path.home() / "SkyCanvas" / "Exports"

EXPORT_DIR.mkdir(parents=True, exist_ok=True)

BACKGROUND = (10, 10, 15)
STAR_COLOR = (255, 220, 0)
LINE_COLOR = (0, 220, 255)
TEXT_COLOR = (180, 180, 180)

FONT_SIZE = 24

CHAR_WIDTH = 15
CHAR_HEIGHT = 30

PADDING_X = 40
PADDING_Y = 40

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_export_path(name, extension):
    timestamp = get_timestamp()

    filename = (f"{name}_{timestamp}.{extension}")

    return EXPORT_DIR / filename

def get_font():

    try:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", FONT_SIZE)
    except:
        return ImageFont.load_default()

def color_line(line):

    output = []

    for char in line:

        if char == "*":
            output.append(
                ("star", char)
            )

        elif char != " ":
            output.append(
                ("line", char)
            )

        else:
            output.append(
                ("empty", char)
            )

    return output

def calculate_size(lines):
    width = 0
    for line in lines:
        width = max(width, len(line))

    height = len(lines)

    return (width * CHAR_WIDTH + PADDING_X * 2, height * CHAR_HEIGHT + PADDING_Y * 2)

def export_image(
    name: str,
    extension: str
):

    lines = get_constellation_lines(name)

    if not lines:

        print(f"[red]Unknown constellation: {name}[/red]")
        return

    width, height = calculate_size(lines)

    image = Image.new("RGB", (width, height), BACKGROUND)

    draw = ImageDraw.Draw(image)
    font = get_font()

    y = PADDING_Y

    for line in lines:

        x = PADDING_X

        for kind, char in color_line(line):

            if kind == "star":
                color = STAR_COLOR

            elif kind == "line":
                color = LINE_COLOR

            else:
                color = BACKGROUND

            draw.text((x, y), char, font=font, fill=color)
            x += CHAR_WIDTH
        y += CHAR_HEIGHT

    path = get_export_path(name, extension)

    if extension.lower() == "jpg":
        image.save(path, "JPEG")

    else:
        image.save(path)

    print(f"[bold green]Exported:[/bold green] {path}")

def export_svg(
    name: str
):

    lines = get_constellation_lines(name)

    if not lines:

        print(

            f"[bold red]Unknown constellation: {name}[/bold red]"

        )

        return

    width, height = calculate_size(

        lines

    )

    svg = []

    svg.append(

        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'

    )

    svg.append(

        f'<rect width="100%" height="100%" fill="rgb{BACKGROUND}"/>'

    )

    y = PADDING_Y

    for line in lines:

        x = PADDING_X

        for kind, char in color_line(line):

            if kind == "star":

                color = (

                    "rgb(255,220,0)"

                )

            elif kind == "line":

                color = (

                    "rgb(0,220,255)"

                )

            else:

                x += CHAR_WIDTH

                continue

            escaped = (

                char

                .replace("&", "&amp;")

                .replace("<", "&lt;")

                .replace(">", "&gt;")

            )

            svg.append(

                f'<text x="{x}" y="{y}" '

                f'font-family="monospace" '

                f'font-size="{FONT_SIZE}px" '

                f'fill="{color}">{escaped}</text>'

            )

            x += CHAR_WIDTH

        y += CHAR_HEIGHT

    svg.append(

        "</svg>"

    )

    path = get_export_path(

        name,

        "svg"

    )

    with open(

        path,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(

            "\n".join(svg)

        )

    print(

        f"[bold green]Exported:[/bold green] {path}"

    )

def export_constellation(name: str, extension:str):

    name = name.lower()

    if name not in CONSTELLATIONS:
        print(f"[bold red]Unknown constellation: {name}[/bold red]")
        return

    if extension == "svg":
        export_svg(name)
    elif extension in ["png", "jpg", "bmp"]:
        export_image(name, extension)
    else:
        print(f"[bold red]Unsupported format: {extension}, you can only export to: JPG, PNG, BMP, SVG[/bold red]")

def export_tonight(extension: str):
    constellations = (get_visible_constellations())

    if not constellations:
        print("[bold yellow]No visible constellations found.[/bold yellow]")
        return

    exported = 0

    for constellation in constellations:
        if constellation not in CONSTELLATIONS:
            continue

        if extension == "svg":
            export_svg(constellation)
        elif extension in ["png", "jpg", "bmp"]:
            export_image(constellation, extension)
        else:
            print(f"[bold red]Unsupported format: {extension}, you can only export to: JPG, PNG, BMP, SVG[/bold red]")
            return
        exported += 1

    print(f"\n[bold green]Exported {exported} constellations.[/bold green]")

def export(target: str, extension: str):
    target = target.lower()
    extension = extension.lower()

    supported_formats = ["png", "jpg", "svg", "bmp"]

    if extension not in supported_formats:
        print(["[bold red]Available formats: JPG, PNG, BMP, SVG[/bold red]"])
        return
    if target == "tonight":
        export_tonight(extension)
    else:
        export_constellation(target, extension)

def export_help():
    print(
        """
[bold cyan]Export usage:[/bold cyan]

[bold yellow]skycanvas --export <target> <format>[/bold yellow]

[bold cyan]Targets:[/bold cyan]

    [-] constellation name
    [-] tonight

[bold cyan]Formats:[/bold cyan]

    [-] JPG
    [-] PNG
    [-] BMP
    [-] SVG

[bold cyan]Examples:[/bold cyan]

    [-] skycanvas --export orion png

    [-] skycanvas --export hydra svg

    [-] skycanvas --export tonight jpg
        """
    )
    