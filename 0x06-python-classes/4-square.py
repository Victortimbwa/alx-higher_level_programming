#!/usr/bin/python3

"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """square class with Private instance attribute: size"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """retrieve the attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """modify the attribute value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
