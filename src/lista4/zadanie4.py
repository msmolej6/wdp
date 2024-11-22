def eratosthenes_sieve(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(n**1 / 2) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    return [i for i, is_prime in enumerate(sieve) if is_prime]


def segmented_sieve(m, n):
    limit = int(n**1 / 2) + 1
    primes = eratosthenes_sieve(limit)

    segment = [1] * (n - m + 1)

    for p in primes:
        start = m if (m % p == 0) else m + (p - m % p)
        if start == p:
            start += p

        for j in range(start, n + 1, p):
            segment[j - m] = 0

    return [i + m for i, prime in enumerate(segment) if prime and m + i > 1]


def palindrom(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1
    return True


def palindromic_primes(m, n):
    primes = segmented_sieve(m, n)

    results = []

    for p in primes:
        if palindrom(str(p)):
            results.append(p)

    return results


if __name__ == "__main__":
    print(str(palindromic_primes(10_000, 20_000)))
