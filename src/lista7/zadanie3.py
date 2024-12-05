from src.shared.file_utils import create_file_path, read_file


def find_longest_text(file_name: str) -> str:
    words = read_words(file_name)
    polish_words = read_popular_words()

    longest_text_length: int = 0
    longest_text: list[str] = []
    current_text_length: int = 0
    current_text: list[str] = []

    for word in words:
        valid_word_length = get_valid_word_length(word, polish_words)
        if valid_word_length >= 0:
            current_text.append(word)
            current_text_length += valid_word_length
        else:
            if current_text_length >= longest_text_length:
                longest_text = current_text
                longest_text_length = current_text_length
            current_text = []
            current_text_length = 0

    if current_text_length >= longest_text_length:
        longest_text = current_text
        longest_text_length = current_text_length

    return " ".join(longest_text)


def get_valid_word_length(word: str, polish_words: set) -> int:
    if len(word) == 1 and word in ";,/?!.-—":
        return 0

    word_to_check = ""

    for ch in word:
        if ch not in ";,/?!.-—":
            word_to_check += ch

    if word_to_check.lower() in polish_words:
        return len(word_to_check)
    return -1


def read_popular_words() -> set:
    file_name = "popularne_slowa2023.txt"
    words = read_words(file_name)
    popular_words: set = set()

    for word in words:
        if not has_forbidden_chars(word):
            popular_words.add(word)

    return popular_words


def has_forbidden_chars(word: str) -> bool:
    forbidden_chars = set("ąćęłńóśźż")

    for w in word:
        if w in forbidden_chars:
            return True

    return False


def read_words(file_name: str) -> list[str]:
    path = create_file_path(__file__, file_name)
    content = read_file(path)

    return content.split()


if __name__ == "__main__":
    file_name = "lalka.txt"
    print(find_longest_text(file_name))
