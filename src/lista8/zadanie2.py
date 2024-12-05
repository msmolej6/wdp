from collections import defaultdict


def is_composable(target: str, word: str) -> bool:
    word_dict = word_to_dict(word)

    for ch in target:
        if ch in word_dict and word_dict[ch] > 0:
            word_dict[ch] -= 1
        else:
            return False

    return True


def word_to_dict(word: str) -> dict[str, int]:
    dictionary: dict[str, int] = defaultdict(int)

    for ch in word:
        dictionary[ch] += 1

    return dictionary


if __name__ == "__main__":
    tests = {
        "kot": "lokomotywa",
        "żak": "lokomotywa",
        "kotka": "lokomotywa",
        "motyl": "lokomotywa",
        "aktyw": "lokomotywa",
    }

    for test in tests.items():
        print(
            f'{test[0]} is'
            f'{'' if is_composable(test[0], test[1]) else ' NOT'} composable from {test[1]}'
        )
