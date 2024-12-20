import numpy


def sieve_of_sundaram(n):
    sieve = numpy.ones(n // 2, dtype=bool)
    i = 1
    j = 1
    while i + j + 2 * i * j <= (n - 1) // 2:
        if not sieve[i]:
            continue
        while i + j + 2 * i * j < (n - 1) // 2:
            sieve[(i + j + 2 * i * j)] = False
            j += 1
        i += 1
        j = i
    return numpy.r_[2, 2 * numpy.nonzero(sieve)[0][1::] + 1], sieve