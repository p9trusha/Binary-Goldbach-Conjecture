import numpy


# решето эратосфена
def sieve_of_eratosthenes(n):
    sieve = numpy.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return numpy.r_[2, 2 * numpy.nonzero(sieve)[0][1::] + 1], sieve
