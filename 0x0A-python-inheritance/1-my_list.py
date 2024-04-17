#!/usr/bin/python3

"""
A class myList inherit from the class list
"""


class MyList(list):
    """
    this class inherit all the attribute and methods of the list class
    """
    def print_sorted(self):
        """
        print_sorted - print element of MyLIst object sorted
        """
        sorted_list = sorted(self)
        print(sorted_list)
