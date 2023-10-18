def calc_z(int maxiter, zs, c):
    """calc output list using Julia update rule"""
    cdef unsigned int i, n
    cdef double complex z
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        while n < maxiter and \
            (z.real * z.real + z.imag * z.imag) < 4:
            z = z * z + c
            n += 1
        output[i] = n
    return output