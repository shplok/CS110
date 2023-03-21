import stdarray
import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primes = _primes(lo, hi)
    # list of primes on int [lo, hi)
    p = _choice(primes)
    q = _choice(primes)
    # sampling two distinct primes
    n = p * q
    m = (p - 1) * (q - 1)
    # list of primes from the int 2, m
    intprimes = _primes(2, m)
    # cycling through intprimes until finding a value "e" that fits criteria
    e = _choice(intprimes)
    while m % e == 0:
        e = _choice(intprimes)
        if m % e != 0:
            return e
    # similarly, an above function cycling through to find value that fits
    d = 1
    while e * d % m != 1:
        d += 1
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, ee):
    return x ** ee % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    primelist = []
    for p in range(lo, hi):
        if p > 1:
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                primelist += [p]
    return primelist


# Returns a list containing a random sample (without replacement) of k items from the list "a".
def _sample(a, k):
    b = []
    for v in a:
        b += [v]

    for i in range(0, k):
        rand = stdrandom.uniformInt(0, k)
        temp = b[rand]
        b[rand] = b[i]
        b[i] = temp
    return b[:k]


# Returns a random item from the list "a".
def _choice(a):
    r = stdrandom.uniformInt(0, len(a))
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
