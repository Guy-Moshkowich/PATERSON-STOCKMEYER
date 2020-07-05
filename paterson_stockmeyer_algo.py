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

def calc_q_r(f, k, p):
    x_to_the_power_of_kp = np.append([1], np.zeros(k*p))
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
    k, p, _ = calc_k_p_m(f)
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
    return [u**(i) for i in range(k)]


def calc_gs(u, k, m):
    '''
    :return: [u^{2k}, u^{4k}, u^{8k}...,u^{2^{m-1}}]
    '''

    return [u**((2**i)*k) for i in range(1, m)]


def calc_k_p_m(f):
    n = len(f) - 1
    k = calc_k(n)
    m = calc_m(n, k)
    p = 2 ** (m - 1)
    return k, p, m

def evaluate(f, u, k, p):

    # validity assertion: if the powers of f are 0,...,k or k*2,...,k*p,...,k*2^(m-1)
    validation_precomputed_powers(f, k, p) # safety net that we do not evaluate polynomials that can't be evaluated from precalculated values. should be removed after algo is completed.
    return np.polyval(f, u) #TODO: replace implementation with one that uses bs and gs precomputed vals.




def ps(f, u): # evaluate a polynomial on an input value for u, using the Paterson-Stockmeyer algorithm.
    '''
    p(x) = [x**(kp)+c(x)]q(x) + [x**(k(p-1)) + s(x)]
    deg(q(x)) = k(p-1)
    deg([x**(k(p-1)) + s(x)]) = k(p-1)
    deg(c(x)) <= k-1 i.e., c(x) can be evaluated
    x**(kp) can be evalauetd
    '''

    n = len(f) - 1
    k, p, m = calc_k_p_m(f)
    q, r = calc_q_r(f, k, p)
    c, s = calc_c_s(r, q, k, p)
    c_val = evaluate(c, u, k, p)
    q_coeff = c_val + u**(k*p)

    bs = calc_bs(u, k)
    gs = calc_gs(u, k, m)

    return c_eval


if __name__ == '__main__':
    u = 5.0
    f = [1, 2, 3, 4]
    print(ps(f,u))
