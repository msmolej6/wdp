import math
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

speed("fastest")
color("black")


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def draw_circle(radius, steps, color):
    step = (2 * math.pi * radius) / steps

    fillcolor(color)
    begin_fill()
    for _ in range(steps):
        fd(step)
        rt(360 / steps)
    end_fill()


def draw_circles(radius, n):
    colors = ["yellow", "green", "violet"]

    new_radius = radius
    move(0, radius)
    for i in range(n):
        draw_circle(new_radius, 60, colors[i % 3])
        new_radius = new_radius - radius / n

    input()


draw_circles(143, 13)
