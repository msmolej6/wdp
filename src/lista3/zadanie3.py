import re


def delete_in_brackets(text):
    lifo = []
    parts = []

    for index, char in enumerate(text):
        if char == '(':
            lifo.append(index)
        if char == ')':
            parts.append(text[lifo.pop():index+1])

    result = text
    if len(parts) == 0:
        return result

    for part in reversed(parts):
        result = result.replace(part, "")

    return result


def delete_in_brackets2(text):
    pattern = r"\([^()]*\)"
    while re.search(pattern, text):
        text = re.sub(pattern, "", text)

    return text


tests = ["Ala ma kota (perskiego)!",
         "Ala ma kota (perskiego) i (nieperskiego)!",
         "Ala ma kota (Ala ma kota (perskiego))!",
         "Ala ma kota (perskiego!",
         "Ala ma kota (Ala ma kota (perskiego)!"]


for test in tests:
    result = delete_in_brackets(test)
    result2 = delete_in_brackets2(test)

    print(f'input: {test}')
    print(f'output: {result}')
    print(f'output2: {result2}')
    print()
