#!/usr/bin/python3
"""
This module contains the Rectangle class
"""

from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle object
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
