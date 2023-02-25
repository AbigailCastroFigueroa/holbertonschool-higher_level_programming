#!/usr/bin/python3
"""Write and save to a json file."""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'
list_created = []

if os.path.exists(file) and os.path.getsize(file) > 0:
    list_created = load_from_json_file(file)
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        list_created.append(i)
save_to_json_file(list_created, file)
