#!/usr/bin/python3
"""It defines a file-writing function."""


def write_file(filename="", text=""):
    """Writing a string to the UTF8 text file.
    Args:
        filename (str): Name the file.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

