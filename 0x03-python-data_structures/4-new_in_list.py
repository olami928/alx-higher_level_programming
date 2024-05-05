#!/usr/bin/python3
# this program changes an element from a list
# without modifyin the original list

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return(my_list)
    else:
        cpy = [x for x in my_list]
        cpy[idx] = element
        return(cpy)
