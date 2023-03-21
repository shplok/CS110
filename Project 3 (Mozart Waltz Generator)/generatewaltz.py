import stdarray
import stdrandom
import stdio


# i go rows left right j columns go ud
minuetMeasure = stdarray.create2D(11, 16, None)
for i in range(11):
    for j in range(16):
        minuetMeasure[i][j] = stdio.readInt()

# in order to find the correct row, you set i equal to the random #
# you can never roll a one and so it goes 2 to 12 inclusive
trioMeasure = stdarray.create2D(6, 16, None)
for i in range(6):
    for j in range(16):
        trioMeasure[i][j] = stdio.readInt()
# setting up two for loops in order to handle the logging and writing of
# the values selected at random.
for k in range(16):
    minuet_random = stdrandom.uniformInt(0, 6) + stdrandom.uniformInt(0, 6)
    stdio.write(str(minuetMeasure[minuet_random][k]) + " ")

for k in range(16):
    trio_random = stdrandom.uniformInt(0, 6)
    stdio.write(str(trioMeasure[trio_random][k]) + " ")
