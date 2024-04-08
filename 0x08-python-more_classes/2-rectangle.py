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

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        return the value of width attribute to caller
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width attribute conditionally
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the value of height attribute to caller
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height attribute conditionally
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle object
        """

        return self.width * self.height

    def perimeter(self):
        """
        return the perimeter of a the rectangle object
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.width)
