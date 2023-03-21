import stdio
import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Accepting each integer value as a command-line argument

y1 = y - (14 - m) // 12
x = y1 + y1 // 4 - y1 // 100 + y1 // 400
m1 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x + 31 * m1 // 12) % 7

# Calculations to determine the day of the week given year month day

stdio.writeln(dow)
