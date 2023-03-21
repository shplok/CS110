import stdio
import sys

k = int(sys.argv[1])
c = float(sys.argv[2])
EPSILON = float(sys.argv[3])
t = c
# Assigning values to k, c, and, EPSILON, also making our guess (t) equal to c

# the formula for calculating the kth root of c up to epsilon decimal places
while abs(1 - c / (t**k)) > EPSILON:
    ft = (t ** k) - c
    ft1 = k * t ** (k - 1)
    t = t - ft / ft1
stdio.writeln(t)
