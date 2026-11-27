#!/usr/bin/python3
"""Module that defines a function to describe an object as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON use."""
    return obj.__dict__
