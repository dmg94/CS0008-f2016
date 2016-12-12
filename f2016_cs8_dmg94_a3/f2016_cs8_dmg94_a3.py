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
#
# Notes:
# MN: you need to test and experiment more with the code
#     pay attention to syntace and logic
#

# MN: what does this function do?
def nice_print(var1, var2):
    # MN: you need to check var1 and var2 separately. what if they are of 2 different types?
    # MN: also you can assume that var1 it is always a string because is a label.
    format_size = ''
    # Here we need a conditional structure to know what data type we have for the format_size
    #if isinstance(var2, str) or (var1, str):
    if isinstance(var2, str):
        # Strings get 30 characters that are truncated if over the limit.
        format_size = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    #elif isinstance(var2, float) or (var1, float):
    elif isinstance(var2, float):
        format_size = '15.4f'
        # Integers get 10 spaces
    #elif isinstance(var2, int) or (var1, int):
    elif isinstance(var2, int):
        format_size = '10d'
        # Here is how I tell Python to print the process_file(fh) function's table.
    # MN: we assume that var is always a string
    #print(format(var1, format_size), " : ", format(var2, format_size))
    print(format(var1, '.30s'), " : ", format(var2, format_size))
    # end nice_print function and if structure
    # Now I am defining a new function named reading_file
    # This function will process each file in the zip file.

# MN: try to open and close files as close as you can
#     first defin the function and than open the file when you are ready to read
# Here I am defining the master_file for the user to give to the program.
#master_file = input('Please give the master file here.')
#fh = open(master_file, 'r')

# MN: define the function first
# MN: make sure to pass arguments in
#def file_input():
def file_input(fh):
    # Defining file_input function. Creating a variable that will store the names in file_names.
    # MN: file_names should be a lits of strings, initialize accordingly
    #file_names = ''
    file_names = []
    # Using a while loop to read the master_file
    # MN: master_file is a string and not a file handle
    #     here you are looping on the letters of the string contained in master_file
    # MN: master_file is used as a global variable. AVOID THAT AT ALL COSTS
    # MN: you define the loop to have l as a loop variable, but you redefine l within loop using master_file
    #     logically is not correct
    #for l in master_file:
    #    # Stripping the \n and using the index to get the length and file names.
    #    l = master_file.rstrip('\n')
    #    file_names = l[0:]

    # MN: to read the names of the data files, you want to open the file for reading and read alll the lines in
    for line in fh:
        file_names.append(line.strip('\n'))

    # Returning the file_names variable for later use in the program.
    return file_names

# This variable is the length of file_names so the computer knows
# how many files there are to read and save.
# MN: here you are checking the length of the list that is returned by the function file_input
#num_files = len(file_input())
# Open the files in read mode
# MN: here you are trying to open a file whos name is returned by the function file_input
# MN: you just called file_input right above. why not store the results from file_input in a variable
#     and use that variable, so you reduce the number of times you read from file
#
#files = open(file_input(), 'r')

# MN: now you can ask for the master list file name, and read the data file names in
master_file = input('Please give the master file here.')
fh = open(master_file, 'r')
files = file_input(fh)
fh.close()

# MN: ...and count the number of files
num_files = len(files)

# Creating an empty list
data = []
total_distance = 0
# In the for loop, I am stripping the newline and splitting the names and distances for the computer.
# MN: as it is written here, you are looping only on the data file names, not on the lines of the files themselves
#for line in files:
#    # Stripping the \n in each line
#    line = line.rstrip('\n')
#    # Splitting the name and the distance pair by the comma of each line
#    # MN: why do you strip '': these means remove nothing from the string
#    lines = line.strip('').split(',')
#    # Adding the lines to the data list
#    data.append(lines)
#    # MN: not sure why you force index to 3
#    index = 3
#    # MN: because here you get an error on the index
#    # MN: if you wanted to get the distance, you should get the 2nd element of the list that has index 1
#    x = lines[index]
#    item = float(x)
#    index += 2
#    # Changing to float each numerical item and assigning it to numbers.
#    total_distance += float(item)
#    # I am assigning total_distance as the total sum of the numbers list
#    # total_lines is the amount of numbers from the files
# MN: where do you open this file
# files.close()

# MN: let's read each data file and insert each line in data
#     Loop on the list "files" which contains the data file names
for file in files:
    # MN: here file contains the name of the data files
    # MN: open the file for reading
    fh = open(file,'r')
    # MN: now we loop on all the lines of the file
    for line in fh:
        # MN: get rid of headers
        if 'distance' in line:
            continue
        # MN: remove \n, split line and convert distance to float
        temp = line.strip('\n').split(',')
        temp[1] = float(temp[1])
        # MN: insert record in data
        data.append(temp)
        # MN: update total distance
        total_distance += temp[1]
    # MN: now you close the file
    fh.close()

# Close files ???
# MN: compute total numnber of lines read
total_lines = len(data)
# Creating an empty dictionary.
directory = {}

# Iterating over the data list to get all of the values
# for each key.
for line in data:
    # Using an if structure to test if the key is already there or not.
    # MN: I guess here you got confused. you need to check if line[0] (the name of the participant) is already in directory
    #     correct?
    #if line[0] in data:
    if line[0] in directory.keys():
        # Adding the next list index for that key into the dictionary
        # if it already exists
        # MN: if you want to append an element to an item that already on the dictionary,
        #     just call the append method on the item
        #directory += directory[line[0]].append[line[1]]
        directory[line[0]].append(line[1])
        # The key will equal the value if it's only in the list once.
    else:
        # MN: you execute this statement only if the name is new
        #     so you need to initialize the element and not assume that is already there
        #directory += directory[line[0]].append[line[1]]
        directory[line[0]] = [line[1]]

# End if structure and for loop.
num_ppl = len(directory)
# Updating directory to include to sum of each value for the
# distance ran by each participant.
updated_dict = {}
# Taking the directory and summing all the values to make
# the updated dictionary
# MN: if you want to iterate on key and value you need to use the method item()
# for key, value in directory():
for key, value in directory.items():
    updated_dict[key] = sum(value)
# End for loop

# MN: define the functions at the beginning. it is really hard to read the flow of the program if you interleave statements and functions
# MN: DO NOT USE globals. pass argument in
#def count():
def count(data_to_count):
    # This function, count, takes the values in the updated_dict() and
    # sums the length of each value.
    # MN: I assume that you are trying to count how many directory have more than one record, correct?
    #num_times = ()
    # MN: I think yo uare using the wrong dictionary
    #for value2 in updated_dict:
    #    # MN: not sure why you use sum and len together
    #    num_times = sum(len(value2))
    # Returns the number of times for the people that are in the files more than once.
    #return num_times
    #
    # MN: loop on all the data passed in and count the lenght of the list of distances
    # MN: initialize outpout variable
    num_part_with_multiple_runs = 0
    for name, values in data_to_count.items():
        if len(values) > 1:
            num_part_with_multiple_runs += 1
    return num_part_with_multiple_runs

# Defining variables needed to find the max and min distance and the name.
max_distance = 0
name_of_max = 0
min_distance = 0
name_of_min = 0
# Using a for loop to iterate over all the keys in the dictionary.
# MN: if you want to irterate on dictioanry keys, you need to use the method keys()
#for key in updated_dict:
for key in updated_dict.keys():
    values = updated_dict[key]
    # Using an if structure to find the max distance ran in the experiments.
    # MN: values is just one float you do not need to sue max
    #if max(values) > max_distance:
    #    max_distance = values
    if values > max_distance:
        max_distance = values
        name_of_max = key
    # MN: same as above
    #elif min(values) in updated_dict:
    #    min_distance = min(values)
    elif values in updated_dict:
        min_distance = values
        name_of_min = key
# Ending for loop and if structure

# Opening up a new file where the names of the directory that
# appeared more than once will be written to,
# how many times they appeared,
# and what their total distance ran was.
# Defining the new file first
# MN: this is a file name and you need to define it as a string
#output_file = f2016_cs8_dmg94_a3.data.output.csv
output_file = 'f2016_cs8_dmg94_a3.data.output.csv'

# Opening the file
# MN: you are opening a file named 'output_file'
#     if you want to use the name that you defined right above, you need to remove the quotes
#opf = open('output_file', 'w')
opf = open(output_file, 'w')
# Writing the keys of the updated dictionary, the number of times
# that each name appears
# and the total distance each person ran.
# MN: with this syntax you are writing the all list of names first and than the rest
#     we want to write one line per name that contains name, runs and distance,
#     so we need to loop
#opf.writelines(str(updated_dict.keys), ",")
#opf.writelines(count(), ',')
#opf.writelines(updated_dict.values + '\n')
for name in updated_dict.keys():
    opf.write(name + ",")
    opf.write(str(directory[name]) + ',')
    opf.writelines(str(updated_dict[name]) + '\n')
# Closing file so it writes and saves it.
opf.close()

# Here I am printing out all of the data for the user to see at the end.
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
print('Please read this file to see '
      'how many times each participants name appears '
      "and their total distance that they ran.")
nice_print('Here is the file to read', output_file)
# End of program!
