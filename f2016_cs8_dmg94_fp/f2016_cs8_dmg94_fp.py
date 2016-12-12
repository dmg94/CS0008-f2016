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

# First I am going to create the Participants class. This will store each participant's