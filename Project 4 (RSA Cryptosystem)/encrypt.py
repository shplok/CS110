import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    en = int(sys.argv[2])
    # accepting n and e as command line arguments
    width = rsa.bitLength(n)
    message = stdio.readAll()
    # calculating width and specifying list for message
    for c in message:
        x = ord(c)
        enc = rsa.encrypt(x, n, en)
        stdio.write(rsa.dec2bin(enc, width))
    stdio.writeln()


if __name__ == '__main__':
    main()
