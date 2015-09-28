FH = input("What is the temprature in fahrenheit? ")
Celsius = (FH - 32) /1.8

print FH, 'Fahrenheit is ' "%.2f" % Celsius, 'degrees Celsius'

Celsius = input('What is the temprature in degrees Celsius? ')
Kelvin = Celsius + 273.15

if Celsius > -273.15:
    print Celsius, 'Celcius is ' "%.2f" % Kelvin, 'degrees Kelvin'

else:
    print "You're at or below absolute zero"


