# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: December 11th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu)
# Description of program:
# This program takes a master file (with multiple file names inside) and loads them into memory.
# Each individual file contains the names of participants and the distances that each of them ran in an experiment.
# After reading the master file, the program will display the following information to the user:
# Number of files read (master_input fct.)
# Total number of lines (process_file fct.)
# Total distance run (by the whole population)
# Total distance run (by each participant name)
# The maximum distance run in the experiment and by whom
# The minimum distance run in the experiment and by whom
# The total number of participants that were in the experiment
# Any participants that appear more than one time, will display the number of times he/she appears and their names.
# In addition to this, an output file will be produced called f2016_cs8_dmg94_fp.output.csv which will be a
# file with the following information:
# Participant name, number of times he/she appeared in the experiment, and their total distance
# with commas separating each value
# Ex) Max,5,3,456.7890

# First I am going to create the Participants class. This will have in memory each participant's name,
# distance that they ran, and the number of runs as the data attributes.
# The methods for the class are as follows:
# init for initializing each participants' properties.
#  get_name which gives the participant's name
#  get_distance which returns the distance that the participant currently ran
# add_distance which adds a single distance (float) for that participant's distance attribute
#  add_Distances which takes in a list and adds it to an accumulator (assuming this is the total distance ran at the
# end for all of the participants together?
# str which prints out that participant's name, distance, and the number of times they ran in a fancy format.

# First I need the class header for the beginning of the program


class Participants:
    # Init method. Uses self, n for name, and d for distance
    def __init__(self, n, d=0):
        # Self.name assigns the name (n) of the participant to the object.
        self.name = n
        # Self.distance assigns the distance (d) for the starting distance ran by the participant.
        self.distance = d
        # This condition tests for the distance amount to set the starting number of runs for that person.
        if d == 0:
            self.runs = 0
        else:
            self.runs = 1
    # End init
    # Defining the next method, get_name

    def get_name(self):
        # This returns the name of the participant when used
        return self.name
    # End get_name
    # Now defining the next method, get_distance

    def get_distance(self):
        # this returns the distance ran (at that moment) when used
        return self.distance
    # End get_distance
    # Next method, add_distance

    def add_distance(self, d):
        # Self.runs is now a counter for the number of runs when add_distance is called.
        self.runs += 1
        # Self.distance is now an accumulator for adding and reassigning the value of the person's distance ran.
        self.distance += d
    # End add_distance
    # Add_Distances is up next

    def add_distances(self, ld):
        # ld is a list of distances ran by the participants?
        for d in ld:
            # This loops over the distances and adds each distance to self.distance
            self.distance += d
            # As well as adds one for each distance counted.
            self.runs += 1
    # Why does add_distance exist if add_distances seems more usable in this assignment?
    # End add_distances method
    # Str method is up next

    def __str__(self):
        # This is where print(participant object) is used
        return "Name : " + format(self.name, '>20.s') + "Distance run : " + format(self.distance, '9.4f') + \
                "Runs : " + format(self.runs, '4d')
        # End of str method
    # this will help in writing to the file of all the participants in output.csv

    def to_csv_file(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
        # End to_csv_file
        # End of class Participants now
# Next in the program I am creating the process_file function which will be used to read each file (made into a list)
#  and add in the \ contents of the dictionary's names and values, which will be used as the individual participants
# later on. It will create a dictionary in output and number of lines.


def process_file(fl):
    # fl is a files list of all the files from the master file
    num_lines = 0
    dictionary = {}
    tot_distance = 0
    for fil in fl:
        fil.rstrip('\n')
        file = open(fil, 'r')
        for line in file:
            # This tests for the header line so it'll skip the line if it is found (first line in each file)
            if 'distance' in line:
                continue
            # This reassigns line to the modified version with the newline stripped and the commas split for each line
            line = line.rstrip('\n').split(",")
            # Assigning key and val to each value in the list of line
            ke, val = line
            # Strips the ending whitespace in each key name.
            k = ke.rstrip()
            # Tests if key is in the dictionary and adds the value in the appropriate place.
            if k in dictionary:
                dictionary[k].append(float(val))
            else:
                dictionary[k] = [float(val)]
            # Counts the number of lines in the file
            num_lines += 1
            # Total distance by adding the values of each line
            tot_distance += float(val)
        # Closes the file at the end.
        file.close()
    # Returns the dictionary and number of lines read by the file
    return dictionary, num_lines, tot_distance
# Next is to get the master file from the user. Going to use the function master_input which will take in
# the file handle and then read it and return a list of the files for process_file to read. mf will be the name for the
# master file taken in input when called.


def master_input(mf):
    # Creating empty list
    file_list = []
    for line in mf:
        line.rstrip('\n')
        # Adding each line to the file_list to be used in process_file().
        file_list.append(line)

    return file_list
# End master_input function
# Now for the main program. First asking for input to give the master file.
master_file = input('Please give the master data file here to be read.')
# Assigning fo to open the master file for the master_input function
fo = open(master_file, 'r')
# Assigning list_files to the output of the master_input function for process_file to use.
list_files = master_input(fo)
# num_files is the length of list_files
num_files = len(list_files)
# Assigning the dictionary and number of lines and total distance from the output of process_file function
n_dict, n_lines, t_distance = process_file(list_files)
# Assigning num_participants to the length of n_dict that was made in process_file function
num_participants = len(n_dict)
# With the dictionary that was just made, now I am going to use a for loop to iterate over n_dict and make
# a list of the class instances to get the number of times each participant ran, the total distance they ran,
# and the minimum and maximum distance (and person for each).
# First making an empty list 'participants'.
participants = {}
min_name = ''
min_distance = 0
max_name = ''
max_distance = 0
# This will be the list of the people that ran more than once stored as a dictionary
appearances = {}
# This for loops takes the blank dictionary, participants, and iterates through n_dict made from process_file fct.
# to instantiate each key and value in the Participants class.
for key, value in n_dict.items():
    # Tests if the key is already in the new dictionary or not
    if not key['name'] in participants.keys():
        # Adds it in as a class instance, pretty sure?
        participants[key['name']] = Participants(key['name'])
    # For every value, it uses the add_distance to add the distances to the new dictionary.
    participants[key['name']].add_distance[value['distance']]
# Now going to find the min and max values with the names by iterating over the new participants dictionary,
# since it will have the values added already.
# Name and distance are the variables here.
for na, obj in participants.items():
    distance = obj.get_distance()
    # Using if structure to determine the min distance and name
    if min_distance > distance:
        min_distance = distance
        min_name = na
        # End first if
    if max_distance < distance:
        max_distance = distance
        max_name = na
        # End second if
    participant_appearances = obj.get_runs
    if participant_appearances not in appearances.keys():
        appearances[participant_appearances] = []
    appearances[participant_appearances].append(na)
    # Ending for loop
# Number of people that have multiple records in the files.
num_ppl_that_ran_multiple = len([1 for item in participants.values() if item.get_runs() > 1])
# Creating output file which will have the records of all of the participants that ran multiple times in the experiment
# with their name, number of times that they ran, and their total distance.
o_file = 'f2016_cs8_dmg94_fp.data.output.csv'
foh = open(o_file, 'w')
foh.write('Name, number of times ran, distance\n')
for name, objects in participants.items():
    foh.write(objects.to_csv_file + '\n')
foh.close()

# Providing output to user now. Format string variables listed below to use in printing
# String format size
f_size_s = '20s'
# Float format size
f_size_f = '12.5f'
# Integer format size
f_size_i = '5d'
print("Number of files read by input     :" + format(num_files, f_size_i))
print("Total number of lines read        :" + format(n_lines, f_size_i))
print('')
print("Total distance run                :" + format(t_distance,f_size_f))
print('')
print("Maximum distance run              :" + format(max_distance, f_size_f))
print("Max distance participant name is  :" + format(max_name, f_size_s))
print('')
print("Minimum distance run              :" + format(min_distance, f_size_f))
print("Min distance participant name is  :" + format(min_name, f_size_s))
print('')
print("Total number of participants      :" + format(num_participants, f_size_i))
print("Number of participants "
      "with multiple records             :" + format(num_ppl_that_ran_multiple, f_size_f))
print("Here is the output file to read "
      "data on the participants that ran multiple times:" + format(o_file, f_size_s))
