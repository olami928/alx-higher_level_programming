#!/usr/bin/python3
# this program replaces a search with a number
def search_replace(my_list, search, replace):
    new_list = [x for x in (my_list)]
    for index in range(len(new_list)):
        if new_list[index] == search:
            new_list[index] = replace
    return (new_list)
