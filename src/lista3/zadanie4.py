from turtle import color, fd, goto, pendown, penup, rt, speed

speed("fastest")
color("black")


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def square(a):
    move(-a / 2, a / 2)

    for _ in range(4):
        fd(a)
        rt(90)


def squares(n, a):
    for i in range(n):
        square(a)
        a = 0.9 * a


squares(20, 400)
input()
