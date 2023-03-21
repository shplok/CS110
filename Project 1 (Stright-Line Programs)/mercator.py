import math
import stdio
import sys

lat = float(sys.argv[1])
lon = float(sys.argv[2])

# ^ Accepting the float values as arguments for latitude and longitude

lat1 = math.radians(lat)

y1 = math.log((1+math.sin(lat1))/(1-math.sin(lat1)))/2
x = lon

# "x" is equal the longitude and "y" is equal to the above equation


stdio.write(x)
stdio.write(" ")
stdio.writeln(y1)

# Writing out the final latitude and longitude listings
