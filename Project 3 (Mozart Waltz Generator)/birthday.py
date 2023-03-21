import stdarray
import stdio
import stdrandom
import sys

DAYS_PER_YEAR = 365

# Accept trials (int) as command-line argument.
trials = int(sys.argv[1])

# Set count, denoting the total number of individuals sampled across the trials number of
# experiments, to 0.
COUNT = 0

for t in range(trials):
    # Perform trials number of experiments, where each experiment involves sampling individuals
    # until a pair of them share a birthday...

    # Set up a 1D list birthdaysSeen of DAYS_PER_YEAR booleans, all set to False by default. This
    # list will keep track of the birthdays encountered in this experiment.
    birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)
    # an array with 365 values, all false until two values are the same
    while True:
        # Sample individuals until match...

        # Increment count by 1.
        COUNT += 1

        # Set birthday to a random integer from [0, DAYS_PER_YEAR).
        birthday = stdrandom.uniformInt(0, DAYS_PER_YEAR)

        if birthdaysSeen[birthday]:
            # For example, in the array of birthdays seen, birthday
            # is a random integer within birthdaysSeen checking to see if any variable is true

            # If birthday has been encountered, abort this experiment, ie, break.
            break
        else:
            # Record the fact that we are seeing this birthday for the first time.
            birthdaysSeen[birthday] = True
            # it then repeats the loop until it finds a value in the array that is also true,
            # then it writes those values

# Write to standard output the average number of people that must be sampled before a match,
# as an int.
stdio.writeln(COUNT // trials)
