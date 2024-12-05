from turtle import (
    begin_fill,
    bk,
    color,
    end_fill,
    fd,
    fillcolor,
    ht,
    lt,
    rt,
    tracer,
    update,
)

colors = [
    "yellow",
    "green",
    "white",
    "turquoise",
    "olive",
    "pink",
    "indigo",
    "magenta",
    "seashell",
    "navy",
]


def build_colors_keys() -> dict[str, int]:
    keys: dict[str, int] = {}

    for index, value in enumerate(colors):
        keys[value[0]] = index

    return keys


def kwadrat(bok, new_color):
    fillcolor(new_color)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def murek(s, bok):
    colors_keys: dict[str, int] = build_colors_keys()
    color_id: int = colors_keys["y"]
    cyclic_color: bool = False

    for a in s:
        if a == "f":
            kwadrat(bok, colors[color_id])
            fd(bok)
        elif a == "b":
            kwadrat(bok, colors[color_id])
            fd(bok)
        elif a == "l":
            bk(bok)
            lt(90)
        elif a == "r":
            rt(90)
            fd(bok)
        elif a == "c":
            cyclic_color = not cyclic_color
        elif a in colors_keys:
            cyclic_color = False
            color_id = colors_keys[a]

        if cyclic_color and a not in ["l", "r"]:
            color_id = (color_id + 1) % len(colors)


def execute_murek(command: str, a: int):
    color("black")
    tracer(0, 0)
    murek(command, a)
    update()


if __name__ == "__main__":
    color("black")
    ht()

    tracer(0, 0)  # szybkie rysowanie
    murek("fffffffffrfffffffffflfffffffffrfffffl", 10)
    murek(4 * "fffffr", 14)
    update()  # uaktualnienie rysunku

    input()
