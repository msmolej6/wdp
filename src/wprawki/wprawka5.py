"""
Dzisiejsze zadanie będzie polegać na stworzeniu palindromu z zadanych liter. sDla przypomnienia: palindromem nazywamy słowo, które czytane od tyłu ma taką samą postać, jak czytane od przodu, przykładowo palindromem jest słowo "kajak".
Celem zadania jest napisanie funkcji, która na wejście przyjmie ciąg znaków, a następnie wypisze na standardowe wyjście najdłuższy palindrom, który można z nich ułożyć.
Przykład
wejście: "abccccdd"
wyjście: "dccaccd"
"""

from collections import defaultdict


def longest_palindrom(word: str) -> str:
    word_dict = defaultdict(int)

    for ch in word:
        word_dict[ch] += 1

    left = ""
    right = ""
    center = ""

    for key in word_dict:
        counter = word_dict[key] // 2

        left = counter * key + left
        right = right + counter * key

        if word_dict[key] - counter * 2 == 1 and center == "":
            center = key

    return left + center + right


if __name__ == "__main__":
    print(longest_palindrom("abccccdd"))
    print(longest_palindrom("blabla"))
    print(longest_palindrom("blablabla"))
    print(longest_palindrom("blablablabla"))
    print(longest_palindrom("blablablablabla"))
