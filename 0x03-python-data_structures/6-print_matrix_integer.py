#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for arr in matrix:
        for item in arr:
            print("{:d}".format(item), end="")
        print()
