# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: November 16th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu)
# Description of program:
# In this program, a zip file is given to the computer (in .csv format).
# After reading the files, the program will give out the following output:
# The total number of participants,
# The number of files read
# The total number of lines read
# The total distance
# The total distance run for each participant
# The max distance (and by whom)
# The min distance (and by whom)
# How many people appear more than once, the number of times that he/she appears
# and their names
# There will also be an output file given to the user to read called
# "f2016_cs8_dmg94_a3.data.output.csv" which will have the following:
# The names of the participants
# The number of times that their name appears in the input files
# The total distance run.
# First I am creating the nice_print function.
# This function will be how the program prints out the table at the end of the program.
# Key is the first data type entry, and value is the second (usually a number)


def nice_print(var1, var2):
    format_size = ''
    # Here we need a conditional structure to know what data type we have for the format_size
    if isinstance(var2, str) or (var1, str):
        # Strings get 30 characters that are truncated if over the limit.
        format_size = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    elif isinstance(var2, float) or (var1, float):
        format_size = '15.4f'
        # Integers get 10 spaces
    elif isinstance(var2, int) or (var1, int):
        format_size = '10d'
        # Here is how I tell Python to print the process_file(fh) function's table.
    print(format(var1, format_size), " : ", format(var2, format_size))
    # end nice_print function and if structure
    # Now I am defining a new function named reading_file
    # This function will process each file in the zip file.
# Here I am defining the master_file for the user to give to the program.

master_file = input('Please give the master file here.')
# Open the file in read mode
files = open(master_file, 'r')
# Creating an empty list
data = []
# In the for loop, I am stripping the newline and splitting the names and distances for the computer.
for line in files:
    # Converting the strings in the file to floats to sum the numbers up.
    numbers = float(line)
    # Stripping the \n in each line
    line = line.rstrip('\n')
    # Splitting the name and the distance pair by the comma of each line
    lines = line.split(',')
    # Adding the lines to the data list
    data.append(lines)
    # I am assigning total_distance as the total sum of the numbers list
    # total_lines is the amount of numbers from the files
    total_distance = sum(numbers)

# Here I am adding the individual lines to the file
#  Numbers is another list that only has the distance numbers
# so they can be added for the total below.
files.close()
# Close files
total_lines = len(data)
# Creating an empty dictionary.
directory = {}
# Iterating over the data list to get all of the values
# for each key.
for line in data:
    # Using an if structure to test if the key is already there or not.
    if line[0] in data:
        # Adding the next list index for that key into the dictionary
        # if it already exists
        directory = directory[line[0]].append[line[1]]
        # The key will equal the value if it's only in the list once.
    else:
        directory[line[0]] = [line[1]]
    count = sum(len(directory.values()))
# End if structure and for loop.
# Updating directory to include to sum of each value for the
# distance ran by each participant.
updated_dict = {}
# Taking the directory and summing all the values to make
# the updated dictionary
for key, value in directory():
    updated_dict[key] = sum(value)

# Defining variables needed to find the max and min distance and the name.
max_distance = 0
name_of_max = 0
min_distance = 0
name_of_min = 0
# Using a for loop to iterate over all the keys in the dictionary.
for key in updated_dict:
    values = updated_dict[key]
    # Using an if structure to find the max distance ran in the experiments.
    if max(values) > max_distance:
        max_distance = max(values)
        name_of_max = key
    elif min(values) in updated_dict:
        min_distance = min(values)
        name_of_min = key
# Ending for loop and if structure
# Opening up a new file where the names of the participants that
# appeared more than once will be written to,
# how many times they appeard
# and what their total distance ran was.
# Defining the new file first
output_file = f2016_cs8_dmg94_a3.data.output.csv
# Opening the file
opf = open(output_file, 'w')





