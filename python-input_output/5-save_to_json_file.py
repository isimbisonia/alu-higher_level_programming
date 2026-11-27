#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a UTF-8 text file using its JSON form."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
