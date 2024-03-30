#!/usr/bin/python3

"""This module provides a class Student
that defines a student by public attribute."""


class Student:
    """
    Defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student object with given
        first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
