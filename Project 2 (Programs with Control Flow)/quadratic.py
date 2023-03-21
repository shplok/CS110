import math
import stdio
import sys

# Accept a (float), b (float), and c (float) as command-line arguments.
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    stdio.writeln("Value of a must not be 0")

    # when using one "=" that is assigning value, but 2 is to compare

else:
    # calculating the discriminant
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        stdio.writeln("Value of discriminant must not be negative")

    else:

        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        # writing root 1 and root 2 in standard output followed by a newline character
        stdio.writeln(str(root1) + " " + str(root2))
