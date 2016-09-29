# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 15th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# The following program tells the user how much /
# butter, sugar, and flour they need
# for a desired amount of cookies given /
# by user input.
# I am starting by making 3 assignment statements /
# one for grams of butter, sugar, and flour per 1 cookie.
Sugar = 6.25
Butter = 5
Flour = 6.875
# Assigning cookies for the number of cookies desired by user input
cookies = int(input('How many cookies do you want to make?'))
# Now I can make an equation to
cookies = Sugar * Butter * Flour
# The user will now get to see how many grams /
# of each ingredient is needed with the /
# following print function.
print('You need: /'
Sugar, 'grams of sugar /'
Flour, 'grams of flour /'
Butter, 'grams of butter')
