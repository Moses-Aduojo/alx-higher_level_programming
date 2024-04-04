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
    def __init__(self, size=0):
        """
        Initializes a new Square object with the specified size.

        Parameters:
            size (int): The length of each side of the square.
        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
