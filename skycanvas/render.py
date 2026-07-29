from skycanvas.coordinates import COORDINATES
from skycanvas.constellations import CONSTELLATIONS
from rich import print
from rich.panel import Panel
import time
import os

WIDTH = 45
HEIGHT = 22

DOTS_PER_CELL_X = 2
DOTS_PER_CELL_Y = 4
DOT_WIDTH = WIDTH * DOTS_PER_CELL_X
DOT_HEIGHT = HEIGHT * DOTS_PER_CELL_Y
BRAILLE_BASE = 0x2800

_BRAILLE_BITS = [
    [0x01, 0x08],
    [0x02, 0x10],
    [0x04, 0x20],
    [0x40, 0x80],
]


def create_canvas():
    return [
        [" " for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]


def create_dot_grid():
    """A higher-resolution sub-pixel grid used to plot smooth lines before
    they get flattened into braille characters on the main canvas."""
    return [
        [False for _ in range(DOT_WIDTH)]
        for _ in range(DOT_HEIGHT)
    ]


def _dot_anchor(x, y):
    """Map a star's canvas cell (x, y) to a sub-pixel coordinate, roughly
    centered within that cell, used as a line endpoint in the dot grid."""
    return x * DOTS_PER_CELL_X + 1, y * DOTS_PER_CELL_Y + 2


def draw_line(dot_grid, x1, y1, x2, y2):
    """Plot a line between two star cells into the sub-pixel dot grid."""

    sx1, sy1 = _dot_anchor(x1, y1)
    sx2, sy2 = _dot_anchor(x2, y2)

    dx = sx2 - sx1
    dy = sy2 - sy1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return

    for i in range(steps + 1):

        x = round(sx1 + dx * i / steps)
        y = round(sy1 + dy * i / steps)

        if 0 <= x < DOT_WIDTH and 0 <= y < DOT_HEIGHT:
            dot_grid[y][x] = True


def _commit_dot_grid(canvas, dot_grid):
    """Flatten the sub-pixel dot grid down into braille characters and
    write them onto the canvas, without overwriting anything already
    drawn there (e.g. a star that happens to sit on a line's path)."""

    for cy in range(HEIGHT):
        for cx in range(WIDTH):

            if canvas[cy][cx] != " ":
                continue

            bits = 0
            base_x = cx * DOTS_PER_CELL_X
            base_y = cy * DOTS_PER_CELL_Y

            for row in range(DOTS_PER_CELL_Y):
                for col in range(DOTS_PER_CELL_X):
                    if dot_grid[base_y + row][base_x + col]:
                        bits |= _BRAILLE_BITS[row][col]

            if bits:
                canvas[cy][cx] = chr(BRAILLE_BASE + bits)


def draw_star(canvas, x, y):

    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[y][x] = "*"



def draw_star_name(canvas, x, y, name):

    label = f" {name}"

    for i, char in enumerate(label):

        pos_x = x + i + 1

        if 0 <= pos_x < WIDTH and 0 <= y < HEIGHT:

            if canvas[y][pos_x] == " ":
                canvas[y][pos_x] = char



def render_canvas(canvas):

    styled_rows = []

    for row in canvas:

        styled_chars = []

        for char in row:

            if char == "*":
                styled_chars.append("[bold yellow]✦[/bold yellow]")

            elif char != " " and BRAILLE_BASE <= ord(char) <= BRAILLE_BASE + 0xFF:
                styled_chars.append(f"[bright_cyan]{char}[/bright_cyan]")

            elif char == " ":
                styled_chars.append(" ")

            else:
                styled_chars.append(f"[dim]{char}[/dim]")

        styled_rows.append("".join(styled_chars))

    print(Panel("\n".join(styled_rows), border_style="blue", padding=(0, 1), expand=False))



def render_constellation(name: str):

    name = name.lower()

    if name not in COORDINATES:
        print(f"Unknown constellation: {name}")
        return


    canvas = create_canvas()
    dot_grid = create_dot_grid()

    stars = COORDINATES[name]

    for star1, star2 in CONSTELLATIONS[name]["connections"]:

        if star1 in stars and star2 in stars:

            x1, y1 = stars[star1]
            x2, y2 = stars[star2]

            draw_line(
                dot_grid,
                x1,
                y1,
                x2,
                y2
            )

    _commit_dot_grid(canvas, dot_grid)

    for star_name, (x, y) in stars.items():

        draw_star(
            canvas,
            x,
            y
        )

        draw_star_name(
            canvas,
            x,
            y,
            star_name
        )


    render_canvas(canvas)

def get_constellation_lines(name: str):
    name = name.lower()

    if name not in COORDINATES:
        return []

    canvas = create_canvas()
    dot_grid = create_dot_grid()
    stars = COORDINATES[name]

    for star1, star2 in CONSTELLATIONS[name]["connections"]:
        if star1 in stars and star2 in stars:
            x1, y1 = stars[star1]
            x2, y2 = stars[star2]

            draw_line(dot_grid, x1, y1, x2, y2)

    _commit_dot_grid(canvas, dot_grid)

    for star_name, (x, y) in stars.items():
        draw_star(canvas, x, y)
        draw_star_name(canvas, x, y, star_name)

    return [
        "".join(row)
        for row in canvas
    ]

def animate_constellation(name: str):

    name = name.lower()

    if name not in COORDINATES:
        print(f"Unknown constellation: {name}")
        return

    stars = COORDINATES[name]
    connections = CONSTELLATIONS[name]["connections"]

    canvas = create_canvas()
    dot_grid = create_dot_grid()

    for star_name, (x, y) in stars.items():
        draw_star(canvas, x, y)
        os.system("clear")
        time.sleep(0.5)

    for star1, star2 in connections:
        if star1 in stars and star2 in stars:

            x1, y1 = stars[star1]
            x2, y2 = stars[star2]

            draw_line(dot_grid, x1, y1, x2, y2)
            _commit_dot_grid(canvas, dot_grid)

            os.system("clear")
            render_canvas(canvas)
            time.sleep(0.5)

    for star_name, (x, y) in stars.items():
        draw_star_name(canvas, x, y, star_name)
        os.system("clear")
        render_canvas(canvas)
        time.sleep(0.5)