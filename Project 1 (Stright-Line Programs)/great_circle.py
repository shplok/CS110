import math
import stdio
import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# accepting the x and y values as command line arguments (float)

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Converting all the values to radians

d = 6359.83*math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))


# The equation for the distance of great circle

# Writing "d", the result of the equation
stdio.writeln(d)
