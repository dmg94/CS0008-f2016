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
partial_total_line = 0
partial_total_dist = 0
total_lines = 0
total_distance = 0
def processFile(fh):
# fh is the variable that is the file handler/object.
    fh = input('Please provide the file name of the first file.' )
    file_object = open ( fh, 'r')
    while fh and fh != 'quit' and fh != 'q'
       for line in file_object:
            partial_total_line += 1
            line = line.rstrip('/n')
            temporary = line.split(',')
            distance = float(temporary[1])
            partial_total_dist += distance
            total_lines += partial_total_line
            total_dist += partial_total_dist
        printkv('File to be read', file_object)
        printkv('Partial # of lines', ptotal_line)
        printkv('Partial distance run', ptotal_dist)
        file = input('Please provide the next file name or enter "q" or "quit" to end.')
        printkv('Total # of lines', total_line)
        printkv('Total distance run', total_dist )
# I assigned file_object to be the variable that will work with the file
  def printkv(key,value,klen=0)
    kl = max(len(key),klen))
    if isinstance (value,str):
        FS = '.30s'
    elif isinstance (value, float):
        FS = '10.3f'
    elif isinstance (value, int):
        FS = '10d'
    print(key(format(key, FS)), value(format(value, FS)))






