#!/usr/bin/python3
"""This function that creates an Object from a “JSON file”"""


import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
jlist = []

if os.path.exists(filename):
    jlist = load_from_json_file(filename)

for index in sys.argv[1:]:
    jlist.append(index)
save_to_json_file(jlist, filename)
