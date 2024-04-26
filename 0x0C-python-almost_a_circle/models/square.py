#!/usr/bin/python3
"""
this module defines a class square that
inherit from the rectangle square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square: defines prototype for a square object
    Attribute:
        inherit all attribute of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialze the attribute of square object"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """set width and heigth to size"""
        self.width = value
        self.height = value
