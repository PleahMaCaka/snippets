#!/usr/bin/python
# -*- coding: utf-8 -*-


import clipboard as cb
import sys

# get argument
file_path = None

"""
ex) > ./cop.py ./example.txt
sys.argv = ['./cop.py', './example.txt']
"""

# no argument
if len(sys.argv) == 1:
    print("Usage: cop <file>")
    exit()
else:
    # check the file extention
    file_path = sys.argv[1]
    have_file_extension = file_path.find(".")
    if have_file_extension == -1:
        # chekc the sure to copy
        print("It is not have file extention | ex) .txt .py .html")
        continue_copy = input("Are you sure to copy? [Y/N]").lower().split()

        yes_words = ['y', 't', 'yes', 'true', 'yeah', 'doit', 'imgay']
        if continue_copy in yes_words:
            pass
        else:
            print("Stop the AwEsOmE copy script.")
            exit()

def get_file_content():
    """
    get content of file in path
    """
    file = open(file_path)
    content_arr = file.readlines()
    file.close()

    result = ""
    for line in content_arr:
        result += line
        
    if result.endswith("\n"):
        result = result[:-1]
    return result

cb.copy(str(get_file_content()))

print(f"{file_path} copied!")
