import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Accepting the x,y,z as command-line arguments

mi = min(x, y, z)
ma = max(x, y, z)
med = (x + y + z) - (mi + ma)

# Calculating the minimum(mi), maximum(ma), and median(med)

stdio.write(mi)
stdio.write(" ")
stdio.write(med)
stdio.write(" ")
stdio.writeln(ma)

# writing the calculations separated by spaces.
