#!/usr/bin/python3
"""This module contains the class Square that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return a specific string format """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute in class Rectangle."""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle """
        return{
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }