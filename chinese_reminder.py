import numpy


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def generate_int(a_param, n_param):
    N = [numpy.prod(n_param)//n_i for n_i in n_param]
    M = []
    for i in range(len(n_param)):
        g, M_i, m_i = gcdExtended(N[i], n_param[i])
        M.append(M_i)
    x = numpy.sum([a_i * N_i * M_i for a_i, N_i, M_i in zip(a_param, N, M)])
    return x


n = [2, 5, 7, 13]
print('n =', n)
n_new = 17
print('n_new =', n_new)
a = [1, 0, 6, 5]
print('a =', a)
x_base = generate_int(a, n)
print('x_base =', x_base)
n_tag = n.copy()
n_tag.append(n_new)
for a_new in range(n_new):
    a_tag = a.copy()
    a_tag.append(a_new)
    x_new = generate_int(a_tag, n_tag)
    if x_new % numpy.prod(n_tag) == x_base % numpy.prod(n):
        print('a_new = ', a_new)
        break

