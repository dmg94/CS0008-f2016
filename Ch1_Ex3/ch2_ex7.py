# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 15th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This is Chapter 2, Exercise 7's program.
# This program asks the user to /
# to enter the number of miles driven /
# and the gallons of gas used.
# Then it converts that into metric and then /
# displays the Kilometres driven, /
# liters used, and the liters per 100 km.
# My first step is assigning miles to user input.
miles = float(input('Enter the total miles driven.'))
# Then, I make an assignment statement for gallons used.
gallons = float(input('Enter how many gallons you used.'))
# Next, I assign kilometres so I can convert miles to kilometers
Kilometers = 1609344 * miles
# Now, I assign liters to convert gallons to liters
Liters = 3.785 * gallons
# I am making the Liters per 100 km equation in this step.
Liter_per_one_hundred_km = 100 * Liters / Kilometers
# Now I get to print out the results for the user.
print('You drove', Kilometers, 'km / '
      'Used', Liters, 'liters / '
      'and have', Liter_per_one_hundred_km, 'liters per100 kilometers')
