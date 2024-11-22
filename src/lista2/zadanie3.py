from math import sqrt


def kolko(n, ofset=0):
    srodek = n//2
    promien = n//2

    for y in range(n):
        print(ofset * 2 * ' ', end=' ')
        for x in range(n):
            odleglosc = sqrt((x - srodek) ** 2 + (y - srodek) ** 2) - 0.5
            if odleglosc <= promien:
                print('#', end='*')
            else:
                print(' ', end=' ')
        print()


def balwan():
    kolko(7, 3)
    kolko(9, 2)
    kolko(13, 0)


balwan()
