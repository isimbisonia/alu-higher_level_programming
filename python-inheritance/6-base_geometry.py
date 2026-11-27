#!/usr/bin/python3
"""Module that defines a base class for geometry shapes."""


class BaseGeometry:
    """Base class for geometry shapes, with an unimplemented area."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")
