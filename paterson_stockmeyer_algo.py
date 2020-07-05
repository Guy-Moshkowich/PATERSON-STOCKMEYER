import math
import logging
import numpy as np
from utils import * # TODO remove after testing as it depends on sympy

logging.basicConfig(level=logging.INFO)
'''
 we will start witk*((2*p)-1)h monic polinomials of degree k(2p-1) where p is a power of 2.
 Assumption: 
 use numpy polynomial's devision and not implemented it here.
 use numpy polymomnial's evaluatation instead of using bs and gs.  
     TODO: use bs and gs for evaluation of polynomials
'''

def calc_q_r(f, k, p): # assuming deg(f)=k(2p-1)
    x_to_the_power_of_kp = np.append([1], np.zeros(k*p))
    print('x_to_the_power_of_kp:')
    print_as_sym(x_to_the_power_of_kp)
    q, r = np.polydiv(f, x_to_the_power_of_kp)
    np.testing.assert_allclose(f, np.polyadd(np.polymul(x_to_the_power_of_kp, q), r))
    return q, r


def calc_c_s(r, q, k, p):
    x_to_the_power_of_kp_minus_one = np.append([1], np.zeros(k*(p-1)))
    r_tilde = np.polysub(r, x_to_the_power_of_kp_minus_one)
    c, s = np.polydiv(r_tilde, q)
    np.testing.assert_allclose(r_tilde, np.polyadd(np.polymul(q, c), s))
    return c, s




def calc_k(n):
    return int(math.sqrt(n/2))


def calc_m(n, k):
    return math.ceil(math.log2(n/k + 1))


def calc_f_tilde(f):
    '''
    assumptions:
    f is monic - later on we need to handle the case that deg(f)=k(2p-1) but noy monic

    '''
    n = f.size - 1
    k, p = calc_k_p(f)
    f_tilde = np.array([1])
    f_tilde = np.pad(f_tilde, (0, k*((2*p)-1) - n - 1), 'constant', constant_values=(0))
    f_tilde = np.append(f_tilde, f)
    return f_tilde


def calc_bs(u, k):
    '''
    bs description in "Improved Bootstrapping for Approximate Homomorphic Encryption" -
    has an error, here is the correct implementation:
    :return: [u^2, u^3, ..., u^k]
    '''
    return [u**(i) for i in range(1, k + 1)]


def calc_gs(u, k, m):
    '''
    :return: [u^{2k}, u^{4k}, u^{8k}...,u^{2^{m-1}}]
    '''

    return [u**((2**i)*k) for i in range(1, m)]

def calc_k_p(f):
    n = len(f) - 1
    k = calc_k(n)
    m = calc_m(n, k)
    p = 2 ** (m - 1)
    return k, p

def calc_val(f, u):

    # validity assertion: if the powers of f are 0,...,k or k*2,...,k*p,...,k*2^(m-1)
    validation_precomputed_powers(f) # safety net that we do not evaluate polynomials that can't be evaluated from precalculated values. should be removed after algo is completed.
    return np.polyval(f, u)


def validation_precomputed_powers(f):
    k, p = calc_k_p(f)
    print('k=' + str(k) + ', p=' + str(p))
    valid_powers = set()
    for i in range(k + 1):
        valid_powers.add(i)
    n = len(f) - 1
    m = calc_m(n, k)
    for i in range(1, m):
        valid_powers.add((2 ** i) * k)
    for i in range(len(f) - 1, -1, -1):
        index = len(f) - i - 1
        assert ((f[i] == 0) or (index in valid_powers)), 'k=' + str(k) + ', p=' + str(p) + ', i=' + str(i) + ', index=' + str(index) + ', valid_powers=' + str(valid_powers) + ', f=' + str(f)


def sp_monic_and_degree(f, u): # evaluate a polynomial on an input value for the variable, given the polynomial's coefficients, using the Paterson-Stockmeyer algorithm.
    '''
    Assumptions:
    f is monic with deg(f)=k(2p-1), p is a 2-power.
    '''
    n = len(f) - 1
    k = calc_k(n)
    m = calc_m(n, k)
    p = 2**(m-1)
    q, r = calc_q_r(f, k, p)
    c, s = calc_c_s(r, q, k, p)
    print_as_sym(f)
    print_as_sym(q)
    print_as_sym(r)
    print_as_sym(c)
    print_as_sym(s)
    c_eval = calc_val(c, u)

    print('c_eval=' + c_eval)
    q_u = sp_monic_and_degree(q, u)


    bs = calc_bs(u, k)
    gs = calc_gs(u, k, m)

    return c_eval


if __name__ == '__main__':
    u = 5.0
    f = [1, 2, 3, 4]
    print(sp_monic_and_degree(f,u))
