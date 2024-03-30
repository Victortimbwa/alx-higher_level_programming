#!/usr/bin/python3

"""This module contains a class Student that defines a student."""


class Student:
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object with
        given first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
