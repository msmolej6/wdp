import random
import turtle

from src.lista7.murek_wdp import build_colors_keys, execute_murek


def move(x: float, y: float):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def get_colors_commands() -> list[str]:
    result: list[str] = []

    for x in build_colors_keys():
        result.append(x)

    return result


def command_one(n):
    color_keys = get_colors_commands()
    command = "f"

    for x in range(n):
        for y in range(n - 1):
            color = color_keys[random.randint(0, len(color_keys) - 1)]
            command += color + "f"

        if x + 1 != n:
            color = color_keys[random.randint(0, len(color_keys) - 1)]
            command += color + ("rfr" if x % 2 == 0 else "lfl")

    return command


def command_two(n):
    command = "yfcfr"

    for i in range(2, n):
        command += i * "f" + "r"

    return command


if __name__ == "__main__":
    a = 15
    n = 15

    move(a * (n + 2) * -1, a * (n + 2))
    execute_murek(command_one(n), a)

    move(n * a / 2, n * a / 2 * -1)
    execute_murek(command_two(n), a)

    input()
