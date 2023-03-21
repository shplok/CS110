import rsa
import stdio
import sys


# Entry point.
def main():
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    # accepting lo and hi as command line arguments
    key = (rsa.keygen(lo, hi))
    # call to rsa.keygen to fill variable "key" and write to standard output
    stdio.write(str(key[0]) + " " + str(key[1]) + " " + str(key[2]))


if __name__ == '__main__':
    main()
