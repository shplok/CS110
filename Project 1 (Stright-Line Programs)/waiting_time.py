import math
import stdio
import sys

a = float(sys.argv[1])
t = float(sys.argv[2])

# a corresponds to average number of events per unit of time, t is time

p = math.exp(-a*t)

# equation to calculate probability

stdio.writeln(p)

# writing the probability followed by a newline character
