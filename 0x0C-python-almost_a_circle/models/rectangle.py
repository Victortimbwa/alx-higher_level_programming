#!/usr/bin/python3
""" Module for Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """returns the current square area"""
        return self.__width * self.__height

    def display(self):
        """ Prints the Rectangle instance with the '#'"""
        for _ in range(self.height):
            print("#" * self.width)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """return a specific string format """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def display(self):
        """ Improved display method to handle x and y """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute in class Rectangle."""
        attr = ['id', 'width', 'height', 'x', 'y']
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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
