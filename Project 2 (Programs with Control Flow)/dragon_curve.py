import stdio
import sys

n = int(sys.argv[1])
# accepting n as an argument
dragon = "F"
nogard = "F"
store = 0
# assigning values to dragon, nogard, and our store variable

# as long as I is in between 1 and n (inclusive), this command switches values of dragon and nogard
#  and notates as L and R
for i in range(1, n + 1):
    store = dragon
    dragon = dragon + "L" + nogard
    nogard = store + "R" + nogard
# then, writing dragon curve in standard output
stdio.writeln(dragon)
