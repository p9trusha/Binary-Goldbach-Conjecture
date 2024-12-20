import numpy


def sieve_quad_form1(sieve, n):
    x = 1
    while 4 * x ** 2 < n:
        y = 1
        qf = 4 * x ** 2 + 1
        while qf < n:
            rem = numpy.mod(qf, 60)
            if (rem == 1 or rem == 13 or rem == 17 or rem == 29 or
                    rem == 37 or rem == 41 or rem == 49 or rem == 53):
                sieve[qf // 2] = not sieve[qf // 2]
            qf += 4 * y + 4
            y += 2
        x += 1
    return sieve


def sieve_quad_form2(sieve, n):
    x = 1
    while 3 * x ** 2 < n:
        y = 2
        qf = 3 * x ** 2 + 4
        while qf < n:
            rem = numpy.mod(qf, 60)
            if rem == 7 or rem == 19 or rem == 31 or rem == 43:
                sieve[qf // 2] = not sieve[qf // 2]
            qf += 4 * y + 4
            y += 2
        x += 2
    return sieve


def sieve_quad_form3(sieve, n):
    x = 1
    while 2 * x ** 2 < n:
        y = x - 1
        qf = 3 * x * x - y * y
        while y > 0:
            if qf >= n:
                qf += 4 * y - 4
                y -= 2
                continue
            rem = numpy.mod(qf, 60)
            if rem == 11 or rem == 23 or rem == 47 or rem == 59:
                sieve[qf // 2] = not sieve[qf // 2]
            qf += 4 * y - 4
            y -= 2
        x += 1
    return sieve


def sieve_of_atkin(n):
    sieve = numpy.zeros(n // 2, dtype=bool)

    sieve = sieve_quad_form1(sieve, n)
    sieve = sieve_quad_form2(sieve, n)
    sieve = sieve_quad_form3(sieve, n)

    for i in range(7, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            for j in range(i * i, n, i * i):
                sieve[j // 2] = False
    sieve[1], sieve[2] = 3, 5
    return numpy.r_[2, 2 * numpy.nonzero(sieve)[0][0::] + 1], sieve
