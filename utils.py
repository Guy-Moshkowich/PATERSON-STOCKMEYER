from sympy import *
import numpy as np

x = symbols('x')


def sym_to_coeffs(f_x):
    f = Poly(f_x, x).all_coeffs()
    return np.array(f, dtype='float64')


def print_as_sym(f):
    f_x = Poly.from_list(f, gens=x)
    pprint(f_x, use_unicode=True)
