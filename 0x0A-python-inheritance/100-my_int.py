#!/usr/bin/python3
"""Contains the definition of the class MyInt."""


class MyInt(int):
    """A representation of a rebel integer class.
    Inherits from int."""

    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the MyInt class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the behavior of the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the behavior of the != operator."""
        return int(self) == other
