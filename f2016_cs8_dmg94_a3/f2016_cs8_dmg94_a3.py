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


def nice_print(key, value):
    # Here we need a conditional structure to know what data type we have for the format_size
    if isinstance(value, str) or (key, str):
        # Strings get 30 characters that are truncated if over the limit.
        format_size = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    elif isinstance(value, float) or (key, float):
        format_size = '15.4f'
        # Integers get 10 spaces
    elif isinstance(value, int) or (key, int):
        format_size = '10d'
        # Here is how I tell Python to print the process_file(fh) function's table.
    print(format(key, format_size), " : ", format(value, format_size))
    # end nice_print function and if structure
    # Now I am defining a new function named reading_file
    # This function will process each file in the zip file.
# Here I am defining the master_file for the user to give to the program.
master_file = input('Please give the master file here.')
# Open the file in read mode
file = open(master_file, 'r')
# Creating an empty list
data = []
# In the for loop, I am stripping the newline and splitting the names and distances for the computer.
for line in file:
    line = line.
    lines = line.
    data.append(line)
    data.remove('name, distance')
# Here I am adding the individual lines to the file
#  Numbers is another list that only has the distance numbers
# so they can be added for the total below.
numbers = float(data[1])
file.close()
# Close files
# I am assigning total_distance as the total sum of the numbers list
total_distance = sum(numbers)
# total_lines is the amount of numbers from the files
total_lines = len(numbers)
directory = dict(data)
for key in directory:
    print(directory.keys)













