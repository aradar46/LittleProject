"""
Title: fileOrganizer.py
Date: 2022-10-16
Author: Arash DR

Description:
    This script can organize files in a directory to the given categories.
    can be use to automate putting a large number of files in desired
    categories.

List of functions:
    pickCategory(suffix): to choose category of file based on suffix
    doCategorize(): to list files in directory and move them to defined folders

List of "non-standard" modules:
    No "non-standard" are used in this program.

Procedure:
    1. Create a dictionary with the categories as keys and suffix as values
    2. Making a function for categorizing based on suffix of files
    3. Making a function to list files in the directory
       and categorize them and move them to defined folders

Usage:
    1- Update dictionary as you with
    2- put fileOrganizer.py in the directory you want to organize
    2- Run : python3 fileOrganizer.py

"""

import os
from pathlib import Path


myCategories = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# A function which returns the category based on the suffix
def pickCategory(suffix):
    for key, value in myCategories.items():
        if suffix in value:
            return key
    return "MISC"  # every other file with suffixes rather than "myCategories"' move in this folder

# We need to find all files in the directory
# in order to categorize them
# using os madule 
# to get path of each item I used path from pathlib

def doCategorize():
    for item in os.scandir(): #for each file in dir
        if item.is_dir():     #precoutious measurement
            continue
        filePath = Path(item) #getting current path of item
        fileType = filePath.suffix.lower() #to get suffix for further steps
        categoryItem = pickCategory(fileType)  # using pickCategory() function
        categoryPath = Path(categoryItem) # making returned category as the path of file #1
        if categoryPath.is_dir() != True: # if the path doesnt exist, so makes it
            categoryPath.mkdir()
        filePath.rename(categoryPath.joinpath(filePath)) # changes the path of file
            
            
doCategorize()
