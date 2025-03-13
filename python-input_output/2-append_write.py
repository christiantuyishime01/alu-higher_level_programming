#!/usr/bin/python3


# Open the file in append mode ("a"), with UTF-8 encoding
def append_write(filename="", text=""):
    # "a" mode ensures the file is created if it doesn't already exist
    with open(filename, "a", encoding="utf-8") as file:
        # Write the text to the end of the file
        # file.write() returns the number of characters written
        return file.write(text)
