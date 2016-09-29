# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 29th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This program takes user input to convert /
# distance and amount of gas used /
# and calculates results in US and Mwtric systems.
# Fuel consumption is also rated by how much gas /
# is used efficiently in liter/100km.
# First I am using user input to figure what system /
# is being used
system = input('What system are you using? Type USC for US and M for Metric')
# Next I am using an If statement to use user input for /
# the distance and amount of gas used.
if system == M:
    gas = float(input( 'Enter the amount of gas used in liters.'))
    distance = float(input( 'Enter the distance traveled in kilometers'))
elif system != M:
    gas = float(input( 'Enter the amount of gas in gallons.'))
    distance = float(input( 'Enter the distance traveled in miles.'))
