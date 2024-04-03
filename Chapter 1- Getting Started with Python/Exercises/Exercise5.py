# Exercise 5: Compute area of Circle
#write a Python program which accepts the radius of a circle from  the user and compute the area.

from math import pi
#the valueof pi is imported to the program used in the area of circle

r=float(input("Input radius of a circle"))
#the variable r is used to store input.

print("the area of the circle with radius" , str(r) ,"is:" , str(pi*r**2))
#the area is then calculated and printed as (output)
