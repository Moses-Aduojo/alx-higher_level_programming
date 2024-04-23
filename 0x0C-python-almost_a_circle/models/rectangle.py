#!/usr/bin/python3
from models.base import Base
"""
this rectangle class inherit from the Base class
"""


class Rectangle(Base):
    """
    this class is prototype for initializing a rectangle object
    Base: the base class from which Rectangle inherit some property
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        "initialize rectangle object instances"
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        width: return the __width attribute of a rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the __width attribute to value
        """
        self.__width = value

    @property
    def height(self):
        """
        hieght: returns the __height attribute of rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height: set the __height attribute to value
        params: value
        """
        self.__height = height

    @property
    def x(self):
        """
        returns the __x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x:  set __x attribute to value
        """
        self.__x = value

    @property
    def y(self):
        """
        returns the __y attribute
        """
        return self.__y

    @x.setter
    def y(self, value):
        """
        y:  set __y attribute to value
        """
        self.__y = value
