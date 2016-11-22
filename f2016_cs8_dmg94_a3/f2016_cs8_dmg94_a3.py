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


def file_input():
    # Defining file_input function. Creating 2 variables that will be the
    # number of files for the computer to read and store the names in file_names.
    file_names = ''
    # Using a while loop to read the master_file
    while master_file != '':
        master_file.readlines()
        # Stripping the \n and using the index to get the length and file names.
        lin = master_file.rstrip('\n')
        file_names = lin[0:]
        # Continues to read lines until the master_file has an empty string.
        master_file.readlines()
    # Returning the file_names and num_files for later on in the program.
    return file_names
# This variable is the length of file_names so the computer knows
# how many files there are to read and save.
num_files = len(file_input())
# Open the files in read mode
files = open(file_input(), 'r')
# Creating an empty list
data = []
# In the for loop, I am stripping the newline and splitting the names and distances for the computer.
for line in files:
    # Stripping the \n in each line
    line = line.rstrip('\n')
    # Splitting the name and the distance pair by the comma of each line
    lines = line.split(',')
    # Adding the lines to the data list
    data.append(lines)
    item = line[1]
    numbers = float(item)
    # I am assigning total_distance as the total sum of the numbers list
    # total_lines is the amount of numbers from the files
    # Converting the strings in the file to floats to sum the numbers up.

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
# End if structure and for loop.
num_ppl = len(directory)
# Updating directory to include to sum of each value for the
# distance ran by each participant.
updated_dict = {}
# Taking the directory and summing all the values to make
# the updated dictionary
total_distance = 0
for key, value in directory():
    updated_dict[key] = sum(value)
    total_distance += float(value)
# End for loop


def count():
    # This function, count, takes the values in the updated_dict() and
    # sums the length of each value.
    num_times = ()
    for value2 in updated_dict:
        num_times = sum(len(value2))
    # Returns the number of times for the people that are in the files more than once.
    return num_times

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
# how many times they appeared,
# and what their total distance ran was.
# Defining the new file first
output_file = f2016_cs8_dmg94_a3.data.output.csv
# Opening the file
opf = open(output_file, 'w')
opf.writelines(updated_dict.keys(), ",", + count() + ',', updated_dict.values + '\n')


nice_print('Number of files read', num_files)
nice_print('Total number of participants', num_ppl)
nice_print('Total lines read', total_lines)
nice_print('Total distance ran by participants is', total_distance)
print('')
nice_print('The maximum distance ran was', max_distance)
nice_print('Person who ran max distance was', name_of_max)
print('')
nice_print('The minimum distance ran was', min_distance)
nice_print('Person who ran min distance was', name_of_min)
print('')
print('Please read this file to see /'
      'how many times each participants name appears /'
      "and their total distance that they ran.")
nice_print('Here is the file to read', output_file)
# End of program!
