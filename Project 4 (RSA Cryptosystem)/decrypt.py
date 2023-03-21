import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    # accepting n and d as command line inputs
    width = rsa.bitLength(n)
    message = stdio.readAll()
    # accepting the encrypted message
    for i in range(0, len(message) - 1, width):
        s = message[i: i + width]
        y = rsa.bin2dec(s)
        dec = rsa.decrypt(y, n, d)
    # decrypting and writing the encrypted message
        decrypts = chr(dec)
        stdio.write(decrypts)


if __name__ == '__main__':
    main()
