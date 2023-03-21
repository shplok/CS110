import stdio
import stdrandom
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# Accept a (int) and b (int) as command-line arguments.

r = stdrandom.uniformInt(a, b)

# Set r to a random integer between a and b, obtained by calling stdrandom.uniformInt().

stdio.writeln(r)

# Write r to standard output.
