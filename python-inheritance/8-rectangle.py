#!/usr/bin/python3
"""Module that defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with a private width and a private height."""

    def __init__(self, width, height):
        """Set the width and height after checking they are valid."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
