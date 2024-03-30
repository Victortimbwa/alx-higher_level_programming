#!/usr/bin/python3
"""
Contains the definition of the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
        - The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
