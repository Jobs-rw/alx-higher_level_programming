#!/usr/bin/python3
"""
This module contains the Square class
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a square object
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square
        """
        return self.__size ** 2
