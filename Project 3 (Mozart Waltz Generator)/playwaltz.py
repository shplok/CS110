import stdaudio
import stdio
import sys

waltzMeasure = stdio.readAllInts()
# reading the 32 numbers from the first problem, now error handling
if len(waltzMeasure) != 32:
    sys.exit("A waltz must contain exactly 32 measures")
for minuteMeasure in waltzMeasure:
    if minuteMeasure < 1 or minuteMeasure > 176:
        sys.exit("A minuet measure must be from [1, 176]")
for trioMeasure in waltzMeasure:
    if trioMeasure < 1 or trioMeasure > 96:
        sys.exit("A trio measure must be from [1, 96]")

# now playing the waltz
for minuetPlay in waltzMeasure[0, 16]:
    filename = "data/M" + str(minuteMeasure)
    stdaudio.playFile(filename)
for trioPlay in waltzMeasure[16, 32]:
    filename = "data/T" + str(trioMeasure)
    stdaudio.playFile(filename)
