import turtle

Coords = tuple[float, float]
Color = tuple[int, int, int]
Pixel = tuple[Coords, Color]


def move(coordinates: Coords):
    turtle.penup()
    turtle.goto(coordinates)
    turtle.pendown()


def draw_square(size: int, color: Color, coordinates: Coords = (0, 0)):
    move(coordinates)

    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(4):
        turtle.fd(size)
        turtle.rt(90)

    turtle.end_fill()


def draw_pixel(size: int, pixel: Pixel):
    draw_square(size, pixel[1], pixel[0])


def get_colors() -> dict[str, Color]:
    return {
        "Bright Red": (255, 0, 0),
        "Bright Green": (0, 255, 0),
        "Bright Blue": (0, 0, 255),
        "Yellow": (255, 255, 0),
        "Cyan": (0, 255, 255),
        "Magenta": (255, 0, 255),
        "Orange": (255, 165, 0),
        "Purple": (128, 0, 128),
        "Lime": (191, 255, 0),
        "Pink": (255, 105, 180),
        "Teal": (0, 128, 128),
        "Navy": (0, 0, 128),
        "Olive": (128, 128, 0),
        "Maroon": (128, 0, 0),
        "Brown": (139, 69, 19),
        "Gold": (255, 215, 0),
        "Silver": (192, 192, 192),
        "Light Gray": (211, 211, 211),
        "Dark Gray": (105, 105, 105),
        "Peach": (255, 218, 185),
        "Turquoise": (64, 224, 208),
        "Mint": (152, 255, 152),
        "Indigo": (75, 0, 130),
        "Crimson": (220, 20, 60),
    }


def get_rgb_colors() -> list[Color]:
    return [color for key, color in get_colors().items()]
