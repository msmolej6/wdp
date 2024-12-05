import turtle

from src.shared.file_utils import create_file_path, read_lines
from src.shared.turtle_utils import (
    Color,
    Coords,
    Pixel,
    draw_pixel,
)

FileRow = list[Color]
FileRows = list[FileRow]
Pixels = list[Pixel]


def draw(rows: FileRows, square_size: int):
    turtle.speed("fastest")
    turtle.colormode(255)
    turtle.tracer(0, 1)

    pixels = convert_to_pixels(rows, square_size)

    for pixel in pixels:
        draw_pixel(square_size, pixel)

    turtle.done()


def convert_to_pixels(rows: FileRows, square_size: int) -> Pixels:
    definitions: Pixels = []

    x_start: float = len(rows) * square_size / 2 * -1
    y_start: float = len(rows[0]) * square_size / 2

    for y in range(len(rows)):
        for x in range(len(rows[0])):
            # treat y as an x, to get better view
            new_x = x_start + y * square_size
            new_y = y_start - x * square_size

            definitions.append((Coords((new_x * -1, new_y)), rows[y][x]))

    return definitions


def convert_to_colors(line: str) -> list[Color]:
    return [eval(item) for item in line.split()]


def read_colors(file_name: str, module_file: str) -> FileRows:
    file_path = create_file_path(module_file, file_name)
    return read_lines(file_path, convert_to_colors)


if __name__ == "__main__":
    file_name = "picture.txt"
    square_size = 10

    lines = read_colors(file_name, __file__)
    draw(lines, square_size)
