# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 15th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This is the Fahrenheit to Celsius converter program.
# It takes user input to convert any Farhernheit temperature /
# Celsius degrees.
# First, I made an assignment statement to use /
# user input for Fahrenheit
Fahrenheit = int(input( 'Enter the temperature in degrees Fahrenheit, please.'))
# Next I am recreating the Fahrenheit to Celsius conversion equation.
celsius = int(5 *(Fahrenheit - 32) / 9)
# Finally, I am printing out the Celsius temperature for the user
print( celsius, 'is the temperature in degrees Celsius.')


