#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list == None:
        return None
    else:
        new_list = my_list[:]
        for i in range(len(new_list) - 1):
            if new_list[i] % 2 == 0:
                new_list[i] = True
            else:
                new_list[i] = False
        return new_list
