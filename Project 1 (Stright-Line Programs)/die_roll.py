import stdio
import stdrandom
import sys

n = int(sys.argv[1])

# Accepts n as the integer being how many sides of the die

d1 = stdrandom.uniformInt(1, n + 1)
d2 = stdrandom.uniformInt(1, n + 1)

# d1 and d2 represent the first and second die with the lowest receiving 1 for the roll and highest
# being n+1 not inclusive.

stdio.writeln(d1 + d2)

# writing the result of d1+d2 in standard output.
