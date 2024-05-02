#!/usr/bin/python3
# this program prints a tuple and len of the words

def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    else:
        return(len(sentence), sentence[0])
