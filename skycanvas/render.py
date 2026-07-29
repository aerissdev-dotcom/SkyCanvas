from skycanvas.coordinates import COORDINATES
from skycanvas.constellations import CONSTELLATIONS
from rich import print

WIDTH = 45
HEIGHT = 22


def create_canvas():
    return [
        [" " for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]


def draw_line(canvas, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return

    if dx == 0:
        char = "│"

    elif dy == 0:
        char = "─"

    elif dx * dy > 0:
        char = "╲"

    else:
        char = "╱"


    for i in range(steps + 1):

        x = round(x1 + dx * i / steps)
        y = round(y1 + dy * i / steps)

        if 0 <= x < WIDTH and 0 <= y < HEIGHT:

            if canvas[y][x] == " ":
                canvas[y][x] = char



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

    for row in canvas:

        line = "".join(row)

        line = line.replace("*", "[bold yellow]*[/bold yellow]")

        print(line)



def render_constellation(name: str):

    name = name.lower()

    if name not in COORDINATES:
        print(f"Unknown constellation: {name}")
        return


    canvas = create_canvas()

    stars = COORDINATES[name]

    for star1, star2 in CONSTELLATIONS[name]["connections"]:

        if star1 in stars and star2 in stars:

            x1, y1 = stars[star1]
            x2, y2 = stars[star2]

            draw_line(
                canvas,
                x1,
                y1,
                x2,
                y2
            )

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
    stars = COORDINATES[name]

    for star1, star2 in CONSTELLATIONS[name]["connections"]:
        if star1 in stars and star2 in stars:
            x1, y1 = stars[star1]
            x2, y2 = stars[star2]

            draw_line(canvas, x1, y1, x2, y2)

    for star_name, (x, y) in stars.items():
        draw_star(canvas, x, y)
        draw_star_name(canvas, x, y, star_name)

    return [
        "".join(row)
        for row in canvas
    ]