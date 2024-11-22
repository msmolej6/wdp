def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(n):
    sequence = [n]

    while n != 1:
        n = f(n)
        sequence.append(n)

    return sequence


def calculate_median(numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    mid = length // 2

    if length % 2 == 0:
        return (numbers[mid] + numbers[mid - 1]) / 2
    else:
        return numbers[mid]


def collatz_analysis(a, b):
    energies = []

    for n in range(a, b + 1):
        seq = collatz_sequence(n)
        print(str(seq))
        energies.append(seq.index(1))

    avg = sum(energies) / len(energies)
    maximum = max(energies)
    minimum = min(energies)
    median = calculate_median(energies)
    print()
    return avg, maximum, minimum, median


if __name__ == "__main__":
    print(str(collatz_analysis(6, 7)))
