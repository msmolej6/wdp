import random
import turtle

from src.lista6.duze_cyfry import daj_cyfre
from src.shared.turtle_utils import (
    Color,
    Coords,
    Pixel,
    draw_pixel,
    get_rgb_colors,
)

Digit = set[Coords]
Digits = dict[int, Digit]
Grid = set[Coords]
colors = get_rgb_colors()


def draw(grid_n: int, square_n: int):
    turtle.speed("fastest")
    turtle.tracer(0, 1)
    turtle.colormode(255)

    pixels = get_pixels(
        get_coloured_digits(get_located_digits(grid_n)), grid_n, square_n
    )

    for pixel in pixels:
        draw_pixel(square_n, pixel)

    turtle.done()


def get_pixels(
    digits: dict[Coords, Color], grid_n: int, square_n: int
) -> set[Pixel]:
    pixels: set[Pixel] = set()

    x_start: float = grid_n * square_n / 2 * -1
    y_start: float = grid_n * square_n / 2

    for xy in digits:
        coords: Coords = (
            x_start + xy[0] * square_n,
            y_start - xy[1] * square_n,
        )
        pixels.add((coords, digits[xy]))

    return pixels


def get_coloured_digits(digits: list[Digit]) -> dict[Coords, Color]:
    filled: dict[Coords, Color] = {}

    for digit in digits:
        color: Color = get_color(filled, digit)
        for xy in digit:
            filled[xy] = color
    return filled


def get_color(digits: dict[Coords, Color], digit: Digit) -> Color:
    neighbours: set[Coords] = set()
    used_colors: set[Color] = set()

    for xy in digit:
        neighbours |= get_neigbours(xy)

    neighbours -= digit

    for xy in neighbours:
        if xy in digits:
            used_colors.add(digits[xy])

    not_used: list[Color] = []
    for color in colors:
        if color not in used_colors:
            not_used.append(color)

    random.shuffle(not_used)
    return not_used.pop()


def get_neigbours(point: Coords) -> set[Coords]:
    points: set[Coords] = {
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    }

    return {
        (x + point[0], y + point[1])
        for x, y in points
        if x + point[0] >= 0 and y + point[1] >= 0
    }


def get_located_digits(grid_size: int) -> list[Digit]:
    digits: Digits = get_digits_coordinates()
    available: list[int] = list(digits.keys())

    grid: Grid = get_grid_coordinates(grid_size)
    new_grid: list[Digit] = []

    while available and grid:
        key = random.choice(available)

        new_xy = get_new_coordinates(digits[key], grid)
        if new_xy:
            new_grid.append(new_xy)
            grid -= new_xy
        else:
            available.remove(key)

    print(len(new_grid))
    return new_grid


def get_new_coordinates(digit: Digit, grid: Grid) -> Digit:
    new_digit = digit
    for xy in grid:
        new_digit = {(x + xy[0], y + xy[1]) for x, y in digit}
        if new_digit <= (grid):
            return new_digit
    return set()


def get_grid_coordinates(size: int) -> Grid:
    return {(x, y) for x in range(size) for y in range(size)}


def get_digits_coordinates() -> Digits:
    return {n: get_digit_coordinates(n) for n in range(10)}


def get_digit_coordinates(digit: int) -> set[Coords]:
    digit_arr = daj_cyfre(digit)
    coordinates: set[Coords] = set()

    for y in range(len(digit_arr)):
        for x in range(len(digit_arr[y])):
            if digit_arr[y][x] == "#":
                coordinates.add((x, y))

    return coordinates


if __name__ == "__main__":
    draw(41, 17)
