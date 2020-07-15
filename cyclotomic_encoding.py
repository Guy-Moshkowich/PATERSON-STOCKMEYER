import cmath as cm
import math as m
import scipy.linalg as linalg
from test_utils import *
'''
We show here how to calculated the coefficient of polynomial in z[x]/(\phi_8(x)) 
for encoding the list of complex numbers: [3+4j, 2-1j]
The result is stated in HEAAN paper to be 0.71x^3 + 2.5x^2 + 1.41x + 2.5

Mathematical details in https://docs.google.com/document/d/18w09HC1UXivOPFzQcH74cYJJmawaY0x3mnjmUIMO20A/edit?usp=sharing
'''
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
print(round_complex_list(actual_coeffs))
print_as_sym(round_complex_list(actual_coeffs)[::-1])