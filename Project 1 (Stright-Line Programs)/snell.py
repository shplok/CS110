import math
import stdio
import sys

theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# accepting the two n values as well as theta as a command line argument

theta11 = math.radians(theta1)

# converting theta into radians (theta 11 symbolizes 1.1 in my mind, and so I can organize easier)

sintheta2 = math.asin((n1/n2) * math.sin(theta11))

theta2 = math.degrees(sintheta2)

# calculating the value for theta 2

stdio.writeln(theta2)
