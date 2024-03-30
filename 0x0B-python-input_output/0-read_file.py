#!/usr/bin/python3

""" This module contains a function that
reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """reads a text file and prints its content."""
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end='')
