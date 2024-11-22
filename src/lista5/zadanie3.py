from random import choice
from turtle import (
    begin_fill,
    color,
    end_fill,
    fd,
    fillcolor,
    goto,
    pendown,
    penup,
    rt,
    speed,
)

from .duze_cyfry import daj_cyfre

speed("fastest")
color("black")


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def draw_square(a, color):
    fillcolor(color)
    begin_fill()

    for _ in range(4):
        fd(a)
        rt(90)
    end_fill()


def draw_digit(d, size, color, x, y):
    digit = daj_cyfre(d)
    a = size / len(digit)

    for i in range(5):
        for j in range(5):
            if digit[i][j] == "#":
                draw_square(a, color)

            x += a
            move(x, y)

        x -= size
        y -= a
        move(x, y)


def draw_number(n, size=100):
    colors = [
        "red",
        "green",
        "blue",
        "yellow",
        "purple",
        "orange",
        "pink",
        "brown",
    ]

    number = str(n)
    x = len(number) * size / 2 * -1
    y = size / 2

    move(x, y)
    for digit in number:
        color = choice(colors)
        draw_digit(int(digit), size, color, x, y)
        x += size + size / 5
        move(x, y)


draw_number(1234567890, 50)
input()
