import random


def find_prime_factors(n: int) -> set[int]:
    factors = set[int]()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 2

    if n > 2:
        factors.add(n)

    return factors


if __name__ == "__main__":
    for n in range(10):
        rand = random.randint(2, 1000)
        factors = find_prime_factors(rand)
        print(rand, str(factors))
