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
# command to write the day of the week if DOW is equal to the number provided.
# after calculated, write the day of the week in standard output
if dow == 1:
    stdio.writeln("Monday")
elif dow == 2:
    stdio.writeln("Tuesday")
elif dow == 3:
    stdio.writeln("Wednesday")
elif dow == 4:
    stdio.writeln("Thursday")
elif dow == 5:
    stdio.writeln("Friday")
elif dow == 6:
    stdio.writeln("Saturday")
elif dow == 0:
    stdio.writeln("Sunday")
else:
    stdio.writeln("Error")
