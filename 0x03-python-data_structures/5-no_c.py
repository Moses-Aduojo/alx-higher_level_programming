#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return
    new_str = []
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str.append(char)
    my_string = "".join(new_str)
    return my_string
