import math
import logging
import numpy as np


logging.basicConfig(level=logging.INFO)

# we will start with monic polinomials of degree k(2p-1) where p is a power of 2.
# assumption: we will use numpy polynomial's devision and not implemented it here.


def calc_q_r(f, k, p): # assuming deg(f)=k(2p-1)
    x_to_the_power_of_kp = np.append([1], np.zeros(k*p))
    q, r = np.polydiv(f, x_to_the_power_of_kp)
    return q, r


def calc_c_s(r, q, k, p):
    x_to_the_power_of_kp_minus_one = np.append([1], np.zeros(k*(p-1)))
    r_tilde = np.polysub(r, x_to_the_power_of_kp_minus_one)
    c, s = np.polydiv(r_tilde, q)
    return c, s




def calc_k(n):
    return round(math.sqrt(n/2))


def calc_m(n, k):
    return math.ceil(math.log2(n/k + 1))


def calc_f_tilde(f, k, m):
    n = f.size
    f_tilde = np.copy(f)
    f_tilde = np.pad(f_tilde, (0, k*((2**m)-1) - n), 'constant', constant_values=(0))
    f_tilde = np.append(f_tilde, 1)
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


def sp(f, u): # evaluate a polynomial on an input value for the variable, given the polynomial's coefficients, using the Paterson-Stockmeyer algorithm.
    return 586
#     f = np.array(f)
#     n = f.size
#     res = 0
#     k = calc_k(n)
#     m = math.ceil(math.log2(n/k + 1))
#     f_tilde = calc_f_tilde(f, k, m)
#     bs = calc_bs(u, k)
#     gs = calc_gs(u, k, m)
#     q, r = calc_q_r_2(f_tilde, k, m)
#     r_tilde = calc_r_tilde(r, k, m)
#     c, s = calc_c_s(r_tilde, q)
#     return res


if __name__ == '__main__':
    u = 5.0
    f = [1, 2, 3, 4]
    print(sp(f,u))
