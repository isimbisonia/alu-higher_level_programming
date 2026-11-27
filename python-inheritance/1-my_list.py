#!/usr/bin/python3
"""Module that defines MyList, a list with a sorted print method."""


class MyList(list):
    """Class that extends the built-in list type."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
