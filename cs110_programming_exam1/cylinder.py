import math
import stdio
import sys

r = float(sys.argv[1])
h = float(sys.argv[2])
# Accepting two floats as command line inputs

S = (2 * math.pi * r)*(r + h)
V = math.pi * (r ** 2) * h
# formulas for calculating Area and Volume
# Writing Area and Volume as standard output
stdio.writeln("S = " + str(S))
stdio.writeln("V = " + str(V))
