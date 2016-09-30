# name: Danielle Grentz
# email: dmg94@pitt.edu
# date: September 29th, 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# TA: Alex Rowden (alex.rowden@pitt.edu)
# This program takes user input to convert /
# distance and amount of gas used /
# and calculates results in US and Metric systems.
# Fuel consumption is also rated by how much gas /
# is used efficiently in liter/100km.
# First I am using user input to figure what system /
# is being used.
system = str(input('What system are you using? Type USC for US or M for Metric'))
# Next I am using an If statement to use user input for /
# the distance and amount of gas used /
# as well as making the conversion equations.
if system == str(' M'):
    liters = float(input('Enter the amount of gas used in liters.'))
    km = float(input('Enter the distance traveled in kilometers'))
    gallons = liters * 3.78541
    miles = km * 1.60934
    mpg = miles / gallons
    liter_per_hundred_km = 100 * liters / km
elif system != str(' M'):
    gallons = float(input('Enter the amount of gas in gallons.'))
    miles = float(input('Enter the distance traveled in miles.'))
    liters = gallons * .264172
    km = miles * .621371
    mpg = gallons / miles
    liter_per_hundred_km = 100 * liters / km
# Now I made another if statement to compare liters/100km /
# to consumption table to give the fuel rating.
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
# Lastly I am making the table for the user /
# to see when they use this program.
print("                           USC              Metric")
print("Distance___________:", format(miles, '12.3f'),'miles', format(km, '12.3f'),'Km')
print("Gas________________:", format(gallons, '12.3f'),'gallons', format(liters, '9.3f'), 'Liters')
print("Consumption________:", format(mpg, '12.3f'),'mpg', format(liter_per_hundred_km, '12.3f'), 'l/100km')

print('Gas Consumption Rating :', fuel)




