import stdio
import stdrandom

rank = stdrandom.uniformInt(2, 15)
suit = stdrandom.uniformInt(1, 5)

# accepting rank and suit as random integers between specified intervals

rankStr = " "
if rank == 14:
    rankStr = "Ace"
elif rank == 13:
    rankStr = "King"
elif rank == 12:
    rankStr = "Queen"
elif rank == 11:
    rankStr = "Jack"
else:
    rankStr = str(rank)

suitStr = " "
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
else:
    suitStr = "Spades"

# Command to assign value to suitStr and rankStr and write in standard output
# with concatenation
stdio.writeln(rankStr + " of " + suitStr)
