#!/usr/bin/python3
"""
This module contains a function that writes a string
to a text file (UTF-8) and returns the number of characters written."""


def write_file(filename="", text=""):
    """ Write a string to a text file and
    return the number of characters written. """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
