#!/usr/bin/python3
"""Module that defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with a private width and height, an area and a description."""

    def __init__(self, width, height):
        """Set the width and height after checking they are valid."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle as [Rectangle] w/h."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
