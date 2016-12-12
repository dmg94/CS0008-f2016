# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: October 29th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu)
# This program takes files from the user and provides them with a running total of
# the distance ran by all of the participants in the file as well as how many lines (people) there
# are in the file as the output by using an indefinite loop until the user puts in 'q' 'quit' or an empty
# string at the end.
# Here I define all the variables that will be used in the functions I am creating.
# They need to start at zero so the partial and Total totals add up correctly.

# MN: variables initialization
total_lines = 0
total_distance = 0
# MN: if you initialize the partial variables here, than you have to declare them global within the function
#     and, also, if you have to loop over multiple files, ther will never be reset to 0 at the beginning of the next file
#     I would define this variable wihtin the function process_file
##partial_total_line = 0
##partial_total_dist = 0
#
# MN: you use fs only in printKV, its initialization should be move in printKV function
##fs = 0

# MN: I will transfer this statment closer where you need to loop to aske the user the next file to be processed
#     Also, I would change the variable name to filename
# fh is the variable that is the file handler/object.
##fh = input("Please enter the first file to be read.")
#
# MN: why do you open the file here? Where do you need to use it
#     this should go inside the main loop. Check below at the end of the program
# Here I am opening the file object provided by the user
##fh = open(fh, 'r')


# Here I am defining the process_file function that I am using.
# MN: the function process_file should be defined with an input argument which is the file object for the file to be processed
##def process_file():
def process_file(fh):
    # MN: DO NOT USE global unless it is really necessary!!!
    #     have you thought about using a local accumulators for the file being processed
    #     and passing the file partials back with a return statment?
    # Here I define the global variables used for this function.
    ##global total_lines
    ##global total_distance
    ##global partial_total_line
    ##global partial_total_dist
    #
    # MN: this file object should be an argument to the function 
    ##global fh

    # MN: initialize local accumulators
    partial_total_line = 0
    partial_total_dist = 0  

    # Here I am using both a while and for loop. The for loop will read the file
    # and the while loop is printing the necessary information.
    for line in fh:
        # This is where I use the local variables to strip the /n in the text file,
        # split the name and distance, and assign the new total and partial total of lines.
        partial_total_line += 1
        line = line.rstrip('/n')
        temporary = line.split(',')
        distance = float(temporary[1])
        partial_total_dist += distance
        #
        # MN: instead of working with globals, just return the partials back with return statment
        ##total_lines += partial_total_line
        ##total_distance += partial_total_dist
        # Printkv function is located below.
        # Here I am printing the file information that was
        # computed in the for loop.
    #
    # MN: while this while loop is here? shouldn't it be outside the process_file function?
    #     the logic of the program is as follow
    #     1) ask for the filename
    #     2) if filename is valid, 
    #     3)   - process the file
    #     4)   - count distance and lines
    #     5)   - update totals
    #     6)   - ask for next filename
    #     7)   - got to step 2
    #     8) user wants to quit
    #     9) print overall totals
    #
    # according to the logic, the while loop on the filename should be surrounding the process_file function 
    ##while fh and fh != 'quit' and fh != 'q':
        ##printkv('File to be read', fh)
        ##printkv('Partial # of lines', partial_total_line)
        ##printkv('Partial distance run', partial_total_dist)
        # Now I need to close the file before I get the next file (or quit).
        ##fh.close()
        ##fh = input('Please provide the next file name or enter "q" or "quit" to end.')
        # Once the program leaves the while loop, the totals need printed.
        ##printkv('Total number of lines', total_lines)
        ##printkv('Total distance run', total_distance)
    #
    # MN: here we processed all the lines of the file
    #     we need to return total partials: number of lines and total distance
    return partial_total_line, partial_total_dist
    #
    # MN: this is the end of process_file


# This is where the printkv function is defined
def printkv(key, value):

    # An if structure is necessary here to tell what values get what formatting size in the output.
    # MN: why do you want to use a global
    ##global fs
    colon = str(":")
    # MN: why do you test on both key and value? you could but you need to have 2 separte if statments: one for the value and one for the key.
    #     think about if you have a key that is a string and a value that is an integer, the format string will work only for one of them.
    ##if isinstance(value, str) or (key, str):
        # Strings get 30 characters that are truncated if over the limit.
        ##fs = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    ##elif isinstance(value, float) or (key, float):
        ##fs = '10.3f'
        # Integers get 10 spaces
    ##elif isinstance(value, int) or (key, int):
        ##fs = '10d'
        # 
        # MN: ?
        # Here is how I tell Python to print the process_file(fh) function's table. 
    ##print(format(key, fs), colon, format(value, fs))

    # MN: you can assume that key is always a string!!!
    if isinstance(value, str):
        # Strings get 30 characters that are truncated if over the limit.
        fs = '.30s'
        # Floats get 10 characters with 3 decimals spots.
    elif isinstance(value, float) or (key, float):
        fs = '10.3f'
        # Integers get 10 spaces
    elif isinstance(value, int) or (key, int):
        fs = '10d'
    
    print(format(key,'.30s'),colon,format(value,fs))
    #
    # MN: this end printKV function


# MN: here we ask the user which is the first file he/she would liket o process
filename = input("Please enter the first file to be read.")
# 
# MN: now we need to loop over the name of the file
while filename and filename != 'quit' and filename != 'q':
    #
    # MN: here we open th efile for reading
    fh = open(filename,'r')
    #
    # MN: than we process the file
    partial_total_line, partial_total_dist = process_file(fh)
    #
    # MN: we processes the file, we can close the file obejct 
    fh.close()
    #
    # MN: now we can print the partials
    printkv('File to read', filename)
    printkv('Partial # of lines', partial_total_line)
    printkv('Partial distance run', partial_total_dist)
    #
    # MN: we need to update the overall accumulators
    total_lines += partial_total_line
    total_distance += partial_total_dist
    #
    # MN: ask user for the following file
    filename = input('Please provide the next file name or press enter or enter "q" or "quit" to end.')
    #
    # MN: end main loop

# MN: when we exit the main loop, the user has expressed the desire to exit
#     we need to print the overall totals
printkv('Total number of lines', total_lines)
printkv('Total distance run', total_distance)

# MN: this call needs to be removed because is outside the main loop (aka verification loop)
##process_file()
# End program
