def koperta(n):
    pierwszy = 0
    dlugosc = 2*n+1
    for x in range(dlugosc):
        for y in range(dlugosc):
            if (x == y or x == pierwszy or y == pierwszy or x == dlugosc-1 or
                    y == dlugosc-1 or x == dlugosc-y-1):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()


koperta(5)
