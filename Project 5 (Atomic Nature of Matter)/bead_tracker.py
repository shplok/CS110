import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]
    # accepting all pixels, tau, delta, and frames as command line input

    # writing the displacement of beads from one frame to another frame
    bf = BlobFinder(Picture(frames[0]), tau)
    prevBeads = bf.getBeads(pixels)
    for i in range(1, len(frames)):
        bf = BlobFinder(Picture(frames[i]), tau)
        currBeads = bf.getBeads(pixels)
        for currBead in currBeads:
            # for each beat currBead in the current frame, identify the prevBead
            # if it is within the radius, write the distance between the two (standard output)
            closest = math.inf
            for prevBead in prevBeads:
                r = currBead.distanceTo(prevBead)
                if r <= delta and r < closest:
                    closest = r
            if closest != math.inf:
                stdio.writef("%.4f\n", closest)
        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
