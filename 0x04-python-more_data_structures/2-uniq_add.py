#!/usr/bin/python3
# this program adds a unique integer
def uniq_add(my_list=[]):
    uniqn = set()
    total = 0
    for num in my_list:
        if num not in uniqn:
            total += num
            uniqn.add(num)
    return (total)
