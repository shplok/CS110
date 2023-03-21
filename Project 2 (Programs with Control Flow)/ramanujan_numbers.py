import stdio
import sys

# accepting n as a command line input
n = int(sys.argv[1])
a = 1
# the formula below for determining if a value has two cubes in two different ways
# if expressible
while a * a * a <= n:
    b = a + 1
    # whilst a^3 is less than or equal to n int, b = a + 1
    while a * a * a + b * b * b <= n:
        c = a + 1
        # whilst a^3 + b^3 is <= n, c = a + 1
        while c * c * c <= n:
            d = c + 1
            # whilst c^3 <= n, then d = c + 1
            while c * c * c + d * d * d <= n:
                x = a * a * a + b * b * b
                y = c * c * c + d * d * d
                # while c^3 + d^3 is <= n, then calculate y
                if x == y:
                    # if x is equal to y, then this statement is run
                    stdio.write(str(x) + " = ")
                    stdio.write(str(a) + "^3 + " + str(b) + "^3 = ")
                    stdio.writeln(str(c) + "^3 + " + str(d) + "^3")
                d += 1
            c += 1
        b += 1
    a += 1
