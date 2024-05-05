#!/usr/bin/python3
# this program deletes a key in a dict
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
