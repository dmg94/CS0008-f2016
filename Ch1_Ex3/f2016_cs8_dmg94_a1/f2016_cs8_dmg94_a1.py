# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 29th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu
# This program takes user input to convert /
# distance and amount of gas used /
# and calculates results in US and Metric systems.
# Fuel consumption is also rated by how much gas /
# is used efficiently in liter/100km.
# First I am using user input to figure what system /
# is being used.
system = input('What system are you using? Type USC for US and M for Metric')
# Next I am using an If statement to use user input for /
# the distance and amount of gas used /
# as well as making the conversion equations.
if system == M:
    gas = float(input( 'Enter the amount of gas used in liters.'))
    distance = float(input( 'Enter the distance traveled in kilometers'))
    usgas = gas * 3.78541
    usdistance = distance * 1.60934
    mpg = usdistance / usgas
    liter_per_hundred_km = 100 * gas / distance
elif not(system == M):
    gas = float(input( 'Enter the amount of gas in gallons.'))
    distance = float(input( 'Enter the distance traveled in miles.'))
    mgas = gas * .264172
    mdistance = distance * .621371
    mpg = gas / distance
    liter_per_hundred_km = 100 * mgas / mdistance
# Now I made another if to compare liters/100km /
# to to consumption table to give the fuel rating.
if liter_per_hundred_km <= 8:
    fuel = "Excellent"
elif liter_per_hundred_km <= 10:
    fuel = "Good"
elif liter_per_hundred_km <= 15:
    fuel = "Average"
elif liter_per_hundred_km <= 20:
    fuel = "Poor"
else:
    fuel = "Extremely poor"




