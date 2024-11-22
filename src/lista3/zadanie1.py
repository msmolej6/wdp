def is_prime(n):
    if n < 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_happy(n):
    return '777' in str(n)


def print_happy():
    happy_numbers_counter = 0

    for n in range(1, 100_001):
        if is_prime(n) and is_happy(n):
            happy_numbers_counter += 1
            print(n, end=' ')

    print(f'\nHappy numbers count: {happy_numbers_counter}')


print_happy()
