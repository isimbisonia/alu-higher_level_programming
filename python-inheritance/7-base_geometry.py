#!/usr/bin/python3
"""Module that defines a base class for geometry shapes."""


class BaseGeometry:
    """Base class for geometry shapes, with an integer validator."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name: the name of the value, always a string.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
