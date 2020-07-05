from sympy import *
import numpy as np

x = symbols('x')


def sym_to_coeffs(f_x):
    f = Poly(f_x, x).all_coeffs()
    return np.array(f, dtype='float64')


def print_as_sym(f):
    f_x = Poly.from_list(f, gens=x)
    pprint(f_x, use_unicode=True)

def validation_precomputed_powers(f, k, m):
    # print('k=' + str(k) + ', m=' + str(m))
    # print_as_sym(f)
    valid_powers = set()
    for i in range(k + 1):
        valid_powers.add(i)
    for i in range(1, m):
        valid_powers.add((2 ** i) * k)
    for i in range(len(f) - 1, -1, -1):
        index = len(f) - i - 1
        cond = (f[i] == 0) or (index in valid_powers)
        if not cond:
            assert true, '\n\n'+ str(np.poly1d(f)) + '\n\n, k=' + str(k)  + ', i=' + str(i) + ', index=' + str(index) + ', valid_powers=' + str(valid_powers) + ', f=' + str(f)
