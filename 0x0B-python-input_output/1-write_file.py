#!/usr/bin/python3
"""
string to a text file (UTF8) and returns the number of characters
"""


def number_of_lines(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
