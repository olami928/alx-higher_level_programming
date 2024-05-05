#!/usr/bin/python3
# this program retuns the best key and value
def best_score(a_dictionary):
    if a_dictionary:
        best_key = None
        best_score = float('-inf')
        for key, value in a_dictionary.items():
            if value > best_score:
                best_key = key
                best_score = value
        return (best_key)
    else:
        return (None)
