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


def generate_candidates(n, k, d):
    if n < k:
        raise ValueError('Argument k must be lower than n')

    if not 0 <= d <= 9:
        raise ValueError('Argument d must be single digit number')

    happiness = k * str(d)
    results = []

    for start in range(n-k+1):

        left = 0
        if start > 0:
            left = 10 ** (start - 1)

        for left_num in range(left, 10 ** start):

            temp = int(str(left_num)+happiness) * (10 ** (n - k - start))

            if n - k - start == 0:
                results.append(temp)
                continue

            for right_num in range(10 ** (n - k - start)):
                results.append(temp+right_num)

    return results


def count_hyperhappy(n, k, d):
    candidates = generate_candidates(n, k, d)

    count = 0
    for number in candidates:
        if is_prime(number):
            count += 1

    print(f'Hyperhappy is a prime number with {k} consecutive {d} digit')
    print(f'There are {count}, {n} - digit hyperhappy numbers')


count_hyperhappy(10, 7, 7)
print()
count_hyperhappy(7, 7, 7)
