#!/usr/bin/python3

"""
This modules defines a class rectangle:
it's attribute and properties are encapsulated
"""


class Rectangle:
    """
    This class provide a a template for the creation of
    a Rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        intitialized Rectangle object properties when a new object is
        created
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        return the value of width attribute to caller
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        set the width attribute conditionally
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif self.width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        return the value of height attribute to caller
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        set the height attribute conditionally
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
