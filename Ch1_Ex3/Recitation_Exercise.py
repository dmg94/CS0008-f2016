# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 15th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This is the program that Alex assigned /
# in recitation. It asks the user to put /
# in a number and then either multiplies /
# it by 3, prints a phrase, or /
# adds 5 depending on the integer.
# First I am going to assign 'number'
# to an input function to get a number from the keyboard
number = int(input("Please enter a random number?"))
# Now I am testing if the number is greater than zero
# When the number is more than 0, it will get /
# multiplied by 3.
if number > 0:
    print(3 * number)
# Now I am testing if the number is equal to zero.
# The following message is printed for zero
elif number == 0:
    print('What a cool number!')
# Lastly, let's test for negative integers
else:
    print(number + 5)
