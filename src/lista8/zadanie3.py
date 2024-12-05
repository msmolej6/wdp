from src.lista8.zadanie2 import word_to_dict
from src.shared.file_utils import create_file_path, read_file


def prepare_pairs(input: str, words: set) -> list[tuple[str, str]]:
    pairs = []

    input_dict = word_to_dict(input.replace(" ", "").lower())

    for word in words:
        word_dict = word_to_dict(word)

        for ch in word:
            if not input_dict[ch] >= word_dict[ch]:
                continue

    return pairs


def is_composable_from_letters(word: str, remaining: dict[str, int]) -> bool:
    for ch in word:
        if ch in remaining and remaining[ch] > 0:
            remaining[ch] -= 1
        else:
            return False

    return True


def read_words(file_name: str) -> set[str]:
    path = create_file_path(__file__, file_name)
    content = read_file(path)

    return set(content.split())


if __name__ == "__main__":
    pass
