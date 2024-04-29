#!/usr/bin/python3
# this program reverse the element of a list

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for j in (my_list):
            print("{:d}".format(j))
        
