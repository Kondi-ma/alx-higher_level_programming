#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    [print('{:d}'.format(j)) for j in reversed(my_list)]
