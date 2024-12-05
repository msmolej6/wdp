import turtle

from src.lista4.zadanie3 import randperm
from src.lista7.zadanie1 import FileRows, convert_to_pixels, read_colors
from src.shared.turtle_utils import draw_pixel


def draw(lines: FileRows, square_size):
    turtle.speed("fastest")
    turtle.colormode(255)
    turtle.tracer(0, 1)

    pixels = convert_to_pixels(lines, square_size)
    shuffled_pixels = randperm(len(pixels))

    for i in shuffled_pixels:
        pixel = pixels[i]
        draw_pixel(square_size, pixel)

    turtle.done()


if __name__ == "__main__":
    square_size = 10
    file_name = "picture.txt"

    lines = read_colors(file_name, __file__)
    draw(lines, square_size)
