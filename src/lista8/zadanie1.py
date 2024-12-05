from collections import defaultdict

from src.shared.file_utils import create_file_path, process_lines, read_file


def translate(phrase: str, dictionary: dict[str, set[tuple[int, str]]]) -> str:
    result: list[str] = []
    for word in phrase.lower().split():
        if word in dictionary:
            eng = dictionary[word]
            most_popular = max(eng)
            result.append(most_popular[1])
        else:
            result.append("[?]")

    return " ".join(result)


def read_dictionary() -> dict[str, set[tuple[int, str]]]:
    brown = read_brown()

    file_path = create_file_path(__file__, "pol_ang.txt")
    pol_eng: dict[str, set[tuple[int, str]]] = defaultdict(lambda: set())

    def line_processor(line: str):
        record = line.split("=")
        if len(record) == 2:
            pol, eng = record
            pol_eng[pol].add((brown[eng], eng))

    process_lines(file_path, line_processor)

    return pol_eng


def read_brown() -> dict[str, int]:
    file_path = create_file_path(__file__, "brown.txt")

    brown = read_file(file_path).lower().split()
    brown_dict: dict[str, int] = defaultdict(int)

    for word in brown:
        for ch in ";,/?!.-—":
            word.replace(ch, "")

        brown_dict[word] += 1

    return brown_dict


if __name__ == "__main__":
    dictionary = read_dictionary()

    # for key, value in dictionary.items():
    #     print(f"{key} : {str(value)}")

    tests = [
        "Zżąć",
        "odcień",
        "Żywy",
        "Chłopiec z dziewczyna pójść do kino",
        "Kobyła mieć mały bok",
    ]

    for test in tests:
        print(f"input: {test}")
        print(f"output: {translate(test, dictionary)}")
        print("dict: ")
        for word in test.lower().split():
            print(f"-- {word}: {str(sorted(dictionary[word], reverse=True))}")
        print()
