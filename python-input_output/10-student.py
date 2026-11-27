#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Class that defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Set the first name, last name and age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        If attrs is a list of strings, only the attributes named in it
        are returned. Otherwise, all attributes are returned.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
