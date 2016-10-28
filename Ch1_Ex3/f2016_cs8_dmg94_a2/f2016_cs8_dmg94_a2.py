# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: October 27th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This program takes files from the user and provides them with a running total of
# the distance ran by all of the participants in the file as well as how many lines (people) there
# are in the file as the output by using an indefinite loop until the user puts in 'q' 'quit' or an empty
# string at the end.
ptotal_line = 0
ptotal_dist = 0
def processFile(fh)
# fh is the variable that is the file handler/object.
    fh = input('Please enter the path of the first file.' )
    file_object = open ( fh, 'r')
# I assigned file_object to be the variable that will work with the file
    while fh and fh != 'quit' and fh != 'q'
        ptotal_dist, ptotal_line = process file(fh)
        Real_total_dist = 0
        Real_total_dist += ptotal_dist
        Real_total_line = 0
        Real_total_line += ptotal_line
    for line in file_object:
        ptotal_line += 1
        line = line.rstrip('/n')
        temporary = line.split(',')
        distance = float(temporary[1])
        ptotal_dist += distance
    printkv('Partial total lines', ptotal_line)
    printkv('Partial total distance', ptotal_dist)
End program




