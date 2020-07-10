import cmath as cm
import math as m
import scipy.linalg as linalg
from test_utils import *


def round_complex(c):
    return round(c.real, 2) + round(c.imag, 2) * 1j


def round_complex_list(l):
    return [round_complex(l_i) for l_i in l]


M = 8
co_primes = [i for i in range(1, M) if m.gcd(i, M) == 1]
N = len(co_primes)
zeta = cm.rect(1, ((2*m.pi)/M))
zeta_matrix = [ [(zeta**i)**n for n in range(N)] for i in co_primes]
zeta_matrix_inverse = linalg.inv(zeta_matrix)
input_1 = 3+4j
input_2 = 2-1j
input = [input_1, input_2, np.conj(input_2), np.conj(input_1)]
actual_coeffs = zeta_matrix_inverse.dot(input)
expected_coeffs = [10/4, m.sqrt(2), 10/4, m.sqrt(2)/2]
np.testing.assert_almost_equal(actual_coeffs, expected_coeffs, decimal=5)
print_as_sym(round_complex_list(actual_coeffs))