#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, item in enumerate(row):
            #  for a given iteration enumerate returns a tuple\
            #  of each item and index
            if i != 0:
                print(" ", end="")
            print("{:d}".format(item), end="")
        print()
