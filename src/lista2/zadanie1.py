def szachownica(n, k):
    for row in range(2 * n):
        for square in range(k):
            for col in range(2 * n):
                if (row + col) % 2 == 0:
                    print(k * ' ', end=' ')
                else:
                    print(k * '#', end=' ')
            print()


szachownica(4, 3)
