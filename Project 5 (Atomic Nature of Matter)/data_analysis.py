import math
import stdio


# Entry point.
def main():
    ETA = 9.135 * (10 ** -4)
    # viscosity of water
    RHO = 0.5 * (10 ** -6)
    # radius of bead
    T = 297.0
    # temp in kelvin
    R = 8.31457
    METERS_PER_PIXEL = 0.175 * (10 ** -6)
    displacements = stdio.readAllFloats()
    var = sum(map(lambda r: (METERS_PER_PIXEL * r) ** 2, displacements)) / (2 * len(displacements))

    # formula to calculate BOLTZMANN constant and AVOGADRO's constant
    BOLTZMANN = 6 * math.pi * var * ETA * RHO / T
    AVOGADRO = R / BOLTZMANN
    stdio.writef("%e %e\n", BOLTZMANN, AVOGADRO)


if __name__ == '__main__':
    main()
