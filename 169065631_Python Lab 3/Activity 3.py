import math
#imports math function

#asks user for diameter and height
Diam = float(input("enter diamter of cylinder here: "))
Height = float(input("Enter the heigt of the cylinder here: "))

#rounds pi to 2 decimal places
pi = 3.1415926535
pi = round(pi, 2)

#calculates radius using diameter/2
Rad = Diam/2

#calculates volume
Vol = pi * Rad**2 * Height

#returns calculated volume to user
print(f"The volume of the cylinder is: {Vol:.2f} cubic units")


