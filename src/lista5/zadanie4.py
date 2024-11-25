def remove_duplicates(list):
    tuples = sorted([(elem, index) for index, elem in enumerate(list)])

    unique_tuples = []
    last_elem = None
    for elem, index in tuples:
        if elem != last_elem:
            unique_tuples.append((elem, index))
            last_elem = elem

    unique_tuples.sort(key=lambda x: x[1])

    return [elem for elem, index in unique_tuples]


if __name__ == "__main__":
    L1 = [1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]

    print("Before", str(L1))

    L2 = remove_duplicates(L1)

    print("After", str(L2))
