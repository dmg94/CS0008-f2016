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
# Number of files read
# Total number of lines read
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
    def __init__(self, n, d):
        self.name = n
        self.distance = d
        # This condition tests for the distance amount to set the starting number of runs for that person.
        if d == 0:
            self.runs = 0
        else:
            self.runs = 1
    #

    def get_name(self):
        return self.name


