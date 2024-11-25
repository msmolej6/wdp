import os
from typing import Callable, TypeVar

T = TypeVar("T")

FILE_NOT_FOUND_ERROR: str = "File {} not found. \n Error: {}"
FILE_IO_ERROR: str = "File {} could not be open. \n Error: {}"


def process_lines(file_path: str, processor: Callable[[str], None]):
    try:
        with open(file_path, "r") as file:
            for line in file:
                processor(line.strip())

    except FileNotFoundError as e:
        print(FILE_NOT_FOUND_ERROR.format(file_path, e.strerror))
    except IOError as e:
        print(FILE_IO_ERROR.format(file_path, e.strerror))


def read_lines(file_path: str, converter: Callable[[str], T]) -> list[T]:
    lines: list[T] = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                lines.append(converter(line.strip()))
            return lines

    except FileNotFoundError as e:
        print(FILE_NOT_FOUND_ERROR.format(file_path, e.strerror))
    except IOError as e:
        print(FILE_IO_ERROR.format(file_path, e.strerror))
    return lines


def read_file(file_path: str) -> list[str]:
    lines: list[str] = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            return lines

    except FileNotFoundError as e:
        print(FILE_NOT_FOUND_ERROR.format(file_path, e.strerror))
    except IOError as e:
        print(FILE_IO_ERROR.format(file_path, e.strerror))

    return lines


def create_file_path(module_file: str, file_name: str) -> str:
    return os.path.join(
        os.path.dirname(os.path.abspath(module_file)), file_name
    )
