import stdio
import sys

n = int(sys.argv[1])
a = 1
b = 1
c = 0
i = 3

# accepting n as standard input, a and b as first two values of fib sequence,
# c as value to store a for transfer "i" is equal to three
# write b in standard output
while i <= n:
    c = a
    a = b
    b = c + b
    i += 1
stdio.writeln(b)
