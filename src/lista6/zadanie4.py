def custom_split(string: str) -> list[str]:
    result: list[str] = []
    part: str = ""

    for ch in string:
        if not ch.isspace():
            part += ch
        else:
            if part != "":
                result.append(part)
            part = ""

    if part != "":
        result.append(part)

    return result


if __name__ == "__main__":
    test = "   Ala    ma    kota ."
    print(test)
    result = custom_split(test)
    print(result)
