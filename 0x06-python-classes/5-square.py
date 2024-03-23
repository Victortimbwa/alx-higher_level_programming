#!/usr/bin/python3

"""a class Square that defines a square by: (based on 4-square.py)"""


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

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """print the square to stdout with xcter ###"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
