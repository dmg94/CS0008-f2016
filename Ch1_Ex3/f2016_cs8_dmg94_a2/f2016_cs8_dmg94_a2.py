# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: October 29th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This program takes files from the user and provides them with a running total of
# the distance ran by all of the participants in the file as well as how many lines (people) there
# are in the file as the output by using an indefinite loop until the user puts in 'q' 'quit' or an empty
# string at the end.
# Here I define all the variables that will be used in the loops of the processFile function
# They need to start at zero so the partial and Total totals add up correctly.
total_lines = 0
total_distance = 0
partial_total_line = 0
partial_total_dist = 0
# This is where the printkv function is defined.


def printkv(key, value, klen=0):

    klen = max(len(key), klen)
    # An if structure is necessary here to tell what values get what formatting size in the output.
    if isinstance (value,str):
        # Strings get 30 characters that are truncated if over the limit.
        fs = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    elif isinstance (value, float):
        fs = '10.3f'
        # Integers get 10 spaces
    elif isinstance (value, int):
        fs = '10d'
        # Here is how I tell Python to print the process_file(fh) function's table.
    print(key(format(key, fs)), value(format(value, fs)))
# Here I am defining the processFile function that I am using.


def process_file(fh= input('Please enter the first file to be read.')):
    # fh is the variable that is the file handler/object.
    global total_lines
    global total_distance
    global partial_total_line
    global partial_total_dist
    fh = input('Please enter the first file to be read.')
    # Here I am opening the file object provided by the user
    file_object = open( fh, 'r')
    while fh and fh != 'quit' and fh != 'q':
        # Here I am using both a while and for loop. The for loop will read the file
        # and the while loop is printing the necessary information.
        for line in file_object:
        # This is where I use the local variables to strip the /n in the text file,
        # split the name and distance, and assign the new total and partial total of lines.
            partial_total_line += 1
            line = line.rstrip('/n')
            temporary = line.split(',')
            distance = float(temporary[1])
            partial_total_dist += distance
            total_lines += partial_total_line
            total_distance += partial_total_dist
# Here is where I use the while loop to print out the table for the user.
# Now I need to have to close the file before I get the next file (or quit).
        file_object.close()
# Printkv function is located above.
    printkv('File to be read', file_object)
    printkv('Partial # of lines', partial_total_line)
    printkv('Partial distance run', partial_total_dist)
    fh = input('Please provide the next file name or enter "q" or "quit" to end.')
# Once the program leaves the while loop, the totals need printed.
    printkv('Total # of lines', total_lines)
    printkv('Total distance run', total_distance)
    process_file(fh)









