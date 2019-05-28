#!/usr/bin/env python3

import os

mypath = input("Enter the directory the files are in: ")
drop = input("Enter text to remove from filename: ")
add = input("Enter text to add to filename: ")

try:
    os.listdir(mypath)
    for filename in os.listdir(mypath):
        if filename.startswith(drop):
            os.rename(mypath + '/' + filename, mypath + '/' + add + filename[len(drop):])

except FileNotFoundError:
    print("The directory doesn't exist.")
