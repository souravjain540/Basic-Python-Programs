# This program pairs 2 objects together using file IO and collections
# For this program to work you must do the following:
# Add a data folder to the directory containing the Pairs.py file
# inside the data folder add a text file named "girls_names.txt" and populate it with as many girl names as you want
# Next, do the same for the text file named "boys_names.txt"
# Now the program should work correctly!
# Note: you can change this program to work with other pairs of objects.

import collections

girl_names = "data/girls_names.txt"
boy_names = "data/boys_names.txt"

# Create a default dict to store the girl and boy names
name_dict = collections.defaultdict(list)

# Read the girl and boy names into the default dict
with open(girl_names, "r") as file:
    for line in file:
        name_dict["girl"].append(line.strip())

with open(boy_names, "r") as file:
    for line in file:
        name_dict["boy"].append(line.strip())

# Pair up the girl and boy names
pairs = zip(name_dict["girl"], name_dict["boy"])

# Iterate over pairs and print the rank and names associated with each rank
for rank, pair in enumerate(pairs):
    girl_name, boy_name = pair
    print(f'Rank {rank + 1}: {girl_name} and {boy_name}')

# Developed by ktriggsdev
