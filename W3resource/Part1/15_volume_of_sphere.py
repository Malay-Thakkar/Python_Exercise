import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * (radius**3)

print("When the radius is {}, the volume is {:.2f}".format(radius, volume))
