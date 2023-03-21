import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])
w = 35.74 + (0.6215 * t) + (0.4275 * t - 35.75) * v ** 0.16
# accepting t and v float values as command line arguments as well as calculating w (windchill)

if t > 50:
    stdio.writeln("Value of t must be <= 50 F")

if v <= 3:
    stdio.writeln("Value of v must be > 3 mph")

# if t is less than 50 or v is less than 3, then one of the respected outputs is written.
# writing the windchill calculation if t is less than or equal to 50 and v is greater than 3
elif t <= 50 and v > 3:
    stdio.writeln(w)
