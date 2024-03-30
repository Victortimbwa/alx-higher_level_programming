#!/usr/bin/python3
"""a class Student that defines a student by: (based on 10-student.py)"""


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
        """
        Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        using the provided json dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
