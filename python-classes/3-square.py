#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square after checking the size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
