#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for i in range(len(my_string) - 1):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]
    return new_str
