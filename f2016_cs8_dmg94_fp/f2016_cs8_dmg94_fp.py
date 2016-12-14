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
        # End of class Participants now
# Next in the program I am creating the process_file function which will be used to read each file (made into a list)
#  and add in the \ contents of the dictionary's names and values, which will be used as the individual participants
# later on. It will create a dictionary in output and number of lines.


def process_file(fl):
    # fl is a files list of all the files from the master file
    num_lines = 0
    dictionary = {}

    for fil in fl:
        file = open(fil, 'r')
        for line in file:
            # This tests for the header line so it'll skip the line if it is found (first line in each file)
            if 'distance' in line:
                continue
            # This reassigns line to the modified version with the newline stripped and the commas split for each line
            line = line.rstrip('\n').split(",")
            # Assigning key and val to each value in the list of line
            key, val = line
            # Strips the ending whitespace in each key name.
            key = key.rstrip()
            # Tests if key is in the dictionary and adds the value in the appropriate place.
            if key in dictionary:
                dictionary[key].append(float(val))
            else:
                dictionary[key] = [float(val)]
            # Counts the number of lines in the file
            num_lines += 1
        # Closes the file at the end.
        file.close()
    # Returns the dictionary and number of lines read by the file
    return dictionary, num_lines
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
master_file = input('Please give the master data file to be read.')
# Assigning fo to open the master file for the master_input function
fo = open(master_file, 'r')
# Assigning list_files to the output of the master_input function for process_file to use.
list_files = master_input(fo)
# num_files is the length of list_files
num_files = len(list_files)
# Assigning the dictionary and number of lines from the output of process_file function
n_dict, n_lines = process_file(list_files)










