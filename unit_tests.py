import unittest
import numpy as np
import paterson_stockmeyer_algo as algo
from sympy import *

x = symbols('x')


def sym_to_coeffs(f_x):
    f = Poly(f_x, x).all_coeffs()
    return np.array(f, dtype='float64')


def print_as_sym(f):
    f_x = Poly.from_list(f, gens=x)
    pprint(f_x, use_unicode=True)


class Tests(unittest.TestCase):

    def test_calc_c_s(self):
        '''
        this test verifies:
        1) correct computation of s(x) and c(x)
        2) s(x) + x**[k(p-1)] is monic with degree k(p-1)
        3) deg(c) <= k -1

        Assumptions: deg(x**k(p-1))=9
        '''

        p = 2**2
        k = 3
        q = sym_to_coeffs(x**15 + 30*x**10 + 25*x**5 +20)
        r = sym_to_coeffs(15*x**15 +10*x**10 +5*x**5 + x + 1)
        c, s = algo.calc_c_s(r, q, k, p)
        expected_c = sym_to_coeffs(15.0)
        expected_s = sym_to_coeffs(-440.0*x**10 - 1.0*x**9 - 370.0*x**5 + 1.0*x - 299.0)
        np.testing.assert_allclose(c, expected_c)
        np.testing.assert_allclose(s, expected_s)


    def test_calc_q_r(self):
        '''
        This test verifies correct computation of r(x) and q(x)
        assumptions:
        deg(f) = k(2p-1) = 5(2*4-1) = 35, k=5, p=2**2=4
        deg(x**(k*p)) = 20
        '''

        k = 5
        p = 2**2
        f_x = x**35 + 30*x**30 + 25*x**25 +20*x**20 +15*x**15 +10*x**10 +5*x**5 + x + 1
        f = sym_to_coeffs(f_x)
        q, r = algo.calc_q_r(f, k, p)
        expected_q = sym_to_coeffs(x**15 + 30*x**10 + 25*x**5 +20)
        expected_r = sym_to_coeffs(15*x**15 +10*x**10 +5*x**5 + x + 1)
        np.testing.assert_allclose(q, expected_q)
        np.testing.assert_allclose(r, expected_r)


    def test_sp(self):
        f = [1, 2, 3, 4]
        u = 5
        algo.sp(f, u)

    # def test_calc_r_tilde(self):
    #     #poly=x^9
    #     #r=x+x^9
    #     r = [0,1,0,0,0,0, 0, 0,0,1]
    #     k = 3
    #     m = 3
    #     r_tilde = algo.calc_r_tilde(r, k, m)
    #     expected_r_tilde = [0, 1]
    #     np.testing.assert_allclose(r_tilde, expected_r_tilde)




    # def test_calc_q_r(self):
    #     f_tilde = [1,0,0,0,0,0, 0, 1]
    #     k = 3
    #     m = 2
    #     q, r = algo.calc_q_r(f_tilde, k, m)  #return f_tilde div x**(k*(2**(m-1)) {x**6}
    #     expected_q = [0, 1]                  #x**7 + 1 = x(x**6) + 1
    #     expected_r = [1]
    #     np.testing.assert_allclose(q, expected_q)
    #     np.testing.assert_allclose(r, expected_r)

    def test_calc_gs(self):
        u = 2
        k = 3
        m = 5
        gs = algo.calc_gs(u, k, m)
        expected_gs = [2**6, 2**12, 2**24, 2**48]
        self.assertEqual(gs, expected_gs)

    def test_calc_bs(self):
        u = 2
        k = 5
        bs = algo.calc_bs(u, k)
        expected_bs = [2, 4, 8, 16, 32]
        self.assertEqual(bs, expected_bs)

    def test_calc_f_tilde(self):
        f = np.array([1, 2, 3])
        k = 3
        m = 2
        f_tilde = algo.calc_f_tilde(f, k, m)
        # polynomial have x**9 {=3*(2**2-1)}  element and so its 10th index should be 1
        expected_f_tilde = np.array([1,2,3,0,0,0,0,0,0,1])
        np.testing.assert_allclose(f_tilde, expected_f_tilde)

    def test_calc_k(self):
        n = 18
        expected_k = 3
        k = algo.calc_k(n)
        self.assertEqual(k, expected_k)

    def test_calc_k_round(self):
        n = 19
        expected_k = 3
        k = algo.calc_k(n)
        self.assertEqual(k, expected_k)

    def test_calc_m(self):
        n = 19
        k = algo.calc_k(n)
        m = algo.calc_m(n,k)
        self.assertTrue(k*(2**m-1) > n)

    # def test_P_div_quotient(self):
    #     quotient, remainder = P.polydiv ([1, 2, 1], (0,1)) # X^2+2x+1 / X
    #     expected_quotient = (2, 1)
    #     expected_remainder = (1)
    #     np.testing.assert_allclose(quotient, expected_quotient)
    #     np.testing.assert_allclose(remainder, expected_remainder)


    def test_poly_div_quotient(self):
        p1 = np.poly1d([1, 2, 1]) # X^2+2x+1
        p2 = np.poly1d([1, 1]) # X+1
        quotient, remainder = np.polydiv(p1, p2)
        quotient_expected =  np.poly1d([1, 1])
        self.assertEqual(quotient, quotient_expected)

    def test_poly_div_remainder(self):
        p1 = np.poly1d([1, 2, 1]) # X^2+2X+1 = X(2+X)+1
        p2 = np.poly1d([1, 0]) # X
        quotient, remainder = np.polydiv(p1, p2)
        quotient_expected = np.poly1d([1, 2])
        reminder_expected =  np.poly1d([1])
        self.assertEqual(quotient, quotient_expected)
        self.assertEqual(remainder, reminder_expected)


if __name__ == '__main__':
    unittest.main()
