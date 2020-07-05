import math
import numpy as np

'''
 Assumption: using numpy polynomial's devision instead of implementing long division.
 
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


def calc_f_tilde(f, k, p):
    x_to_the_power_of_kp = np.append([1], np.zeros(k * (2*p - 1)))
    f_tilde = np.polyadd(f, x_to_the_power_of_kp)
    return f_tilde


def calc_k_p_m(f):
    n = deg(f)
    k = calc_k(n)
    m = calc_m(n, k)
    p = 2 ** (m - 1)
    return k, p, m


def evaluate_deg_less_than_k(f, u, k, p, precomputed_u_powers):
    assert deg(f) <= k
    result = 0
    for i in range(len(f)):
        u_power_i = precomputed_u_powers[i]
        coeff_power_i = f[len(f) - i - 1]
        result += coeff_power_i*u_power_i
    assert result == np.polyval(f, u)
    return result


def deg(f):
    return len(f) - 1


def precomputed_u_powers_less_than_k(u, k):
    results = [1]
    for i in range (1, k+1):
        results.append(results[i - 1]*u)
    return results


def precomputed_u_two_powers(u, k, p):
    results = [1, u**(2*k)]
    for i in range (2, k+1):
        u_power = results[i - 1]**2
        assert u_power == u**((2**i)*k), 'i='+str(i)+', 2**i=' + str(2**i)
        results.append(u_power)
    return results


def ps(f, u):
    k, p, m = calc_k_p_m(f)
    f_tilde = calc_f_tilde(f, k, p)
    f_tilde_val_in_u = ps_recursive(f_tilde, u, k, p, precomputed_u_powers_less_than_k(u, k), precomputed_u_two_powers(u, k, p))
    f_val_in_u = f_tilde_val_in_u - u**(k*(2*p - 1))
    return f_val_in_u


def ps_recursive(f, u, k, p, precomputed_u_powers_less_than_k, precomputed_u_two_powers):
    '''
    p(x) = [x**(kp)+c(x)]q(x) + [x**(k(p-1)) + s(x)]
    deg(q(x)) = k(p-1)
    deg([x**(k(p-1)) + s(x)]) = k(p-1)
    deg(c(x)) <= k-1 i.e., c(x) can be evaluated
    x**(kp) can be evaluated
    '''

    n = deg(f)
    if n <= k:
        return evaluate_deg_less_than_k(f, u, k, p, precomputed_u_powers_less_than_k)
    q, r = calc_q_r(f, k, p)
    c, s = calc_c_s(r, q, k, p)
    c_val = evaluate_deg_less_than_k(c, u, k, p, precomputed_u_powers_less_than_k)
    q_coeff = c_val + precomputed_u_two_powers[int(math.log2(p))]
    x_power_kp_minus_one = np.append([1], np.zeros(k*(p-1)))
    s_plus_x_power_kp_minus_one = np.polyadd(x_power_kp_minus_one,s)
    assert deg(q) == k*(p-1)
    assert deg(s_plus_x_power_kp_minus_one) == k*(p-1)
    q_val = ps_recursive(q, u, k, p//2, precomputed_u_powers_less_than_k, precomputed_u_two_powers)
    s_plus_x_power_kp_minus_one_val = ps_recursive(s_plus_x_power_kp_minus_one, u, k, p // 2, precomputed_u_powers_less_than_k, precomputed_u_two_powers)
    return q_coeff*q_val + s_plus_x_power_kp_minus_one_val


if __name__ == '__main__':
    u = 5.0
    f = [4,3,2,1]
    print(ps(f,u))
