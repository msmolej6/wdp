from random import randint


def randperm(n):

    numbers = [i for i in range(n)]

    for i in range(n-1, 0, -1):
        j = randint(0, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


# print(str(randperm(9)))

# print(str(randperm(10 ** 6)))
