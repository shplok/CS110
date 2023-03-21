from quadratic import Quadratic
import stdio
import sys


# Entry point.
def main():
    x = float(sys.argv[1])
    while not stdio.isEmpty():
        a = stdio.readFloat()
        b = stdio.readFLoat()
        c = stdio.readFloat()
        q = Quadratic(a, b, c)
        stdio.writef("%s; %f; %s; %f; %f\n", q, q[x], q.roots(), q.sum(), q.prod())


if __name__ == '__main__':
    main()
