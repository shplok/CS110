import stdio


sqr = 0
# Setting the sum of squares equal to 0
while not stdio.isEmpty():
    x = stdio.readInt()
    sqr += x ** 2
# reading the integers given and adding the squares to the sum of squares var
# writing the sum of squares as standard output
stdio.writeln(sqr)
