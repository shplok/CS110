import stdio
import sys

n = int(sys.argv[1])
# accepting n as a system argument
# for "i" in the range of [2,n], calculate the total
for i in range(2, n + 1):
    total = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            total += j
    # if the total is equal to i, then write total. Total being a perfect number
    if total == i:
        stdio.writeln(total)
