import os
from typing import Optional


def find_reversed_pairs(words: list[str]) -> dict[str, str]:
    pairs: dict[str, Optional[str]] = {}

    for word in words:
        if word in pairs:
            continue
        if word[::-1] in pairs:
            pairs[word[::-1]] = word
            continue

        pairs[word] = None

    return {key: value for key, value in pairs.items() if value is not None}


if __name__ == "__main__":
    file_name = "popularne_slowa2023.txt"

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), file_name
    )

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            pairs = find_reversed_pairs(lines)

            for pair in pairs.items():
                print(pair[0], pair[1])

    except FileNotFoundError:
        print("{} not found".format(file_name))
    except IOError:
        print("I/O error")
