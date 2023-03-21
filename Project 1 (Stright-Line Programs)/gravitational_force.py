import stdio
import sys

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# Accepting the float value of each command line argument as a certain variable

G = 6.674*10**-11

# equation for grav

f = G*(m1*m2)/r**2

# equation for determining gravitational force

# writing force with a new line character at the end.
stdio.writeln(f)
