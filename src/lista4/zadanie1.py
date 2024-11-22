import math
from turtle import (
    begin_fill,
    color,
    end_fill,
    fd,
    fillcolor,
    goto,
    lt,
    pendown,
    penup,
    rt,
    speed,
)

speed("fastest")
color("black")


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def draw_cirlce(radius, steps):
    step = (2 * math.pi * radius) / steps

    fillcolor("yellow")
    begin_fill()
    for _ in range(steps):
        fd(step)
        rt(360 / steps)
    end_fill()


def draw_rectangle(a, b, color):
    fillcolor(color)
    begin_fill()
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    fd(a)
    rt(90)
    fd(b)
    end_fill()


def draw_rectangles(radius, steps):
    rectangle_colors = ["red", "orange", "green", "blue"]

    b = (2 * math.pi * radius) / steps
    max_a = 3.0 * radius

    for i in range(steps):
        color = rectangle_colors[i % 4]
        a = max_a - (max_a / steps) * (steps - 1 - i)
        draw_rectangle(a, b, color)
        rt(180)
        fd(b)
        rt(360 / steps - 90)


def draw(radius, steps):
    move(0, radius)
    draw_cirlce(radius, steps)
    lt(90)
    draw_rectangles(radius, steps)
    input()


draw(72, 36)
