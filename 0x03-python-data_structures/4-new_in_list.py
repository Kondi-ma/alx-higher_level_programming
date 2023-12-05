#!/usr/bin/python3
def new_in_list(my_list, idx, element):
     n_list = my_list[:idx]
    if 0 <= idx < len(my_list):
        n_list[idx] = element
        return(n_list)
    return(my_list)

