#!/usr/bin/python3


"""
This module provides functions and class for geometric shape.

Contents:
- Square: a square class.
"""


class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The size of each side of the square.

    Methods:
        None
    """
    def __init__(self, size):
        """
        Initializes a new Square object with the specified size.

        Parameters:
            size (int): The length of each side of the square.
        """
        self.__size = size
