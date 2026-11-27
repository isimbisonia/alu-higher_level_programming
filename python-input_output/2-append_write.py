#!/usr/bin/python3
"""Module that defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append text to the end of a UTF-8 file and return its length."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
