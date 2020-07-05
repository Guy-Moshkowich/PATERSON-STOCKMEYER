import unittest
import numpy as np
import paterson_stockmeyer_algo as algo
from utils import *





class Tests(unittest.TestCase):

    def test_sp_monic_and_degree(self):
        f_x = x ** 60 + 50 * x ** 50 + 40 * x ** 40 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        u = 2
        val = algo.sp_monic_and_degree(f, u)
        print('val=' + str(val))

    def test_calc_c_s(self):
        '''
        this test verifies:
        1) correct computation of s(x) and c(x)
        2) s(x) + x**[k(p-1)] is monic with degree k(p-1)
        3) deg(c) <= k -1

        Assumptions: deg(x**k(p-1))=9
        '''
        f_x = x ** 60 + 50 * x ** 50 + 40 * x ** 40 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        n = len(f) - 1
        k = algo.calc_k(n) #k=5
        m = algo.calc_m(n, k)
        p = 2 ** (m - 1) # p=8
        q = sym_to_coeffs(x**20 + 50.0*x**10 + 40.0)
        r = sym_to_coeffs(10.0*x**10 + 5.0*x**5 + 1.0*x + 1.0)
        c, s = algo.calc_c_s(r, q, k, p)
        expected_c = sym_to_coeffs(-1.0*x**15 + 50.0*x**5)
        expected_s = sym_to_coeffs(-2460.0*x**15 + 10.0*x**10 - 1995.0*x**5 + 1.0*x + 1.0)
        np.testing.assert_allclose(c, expected_c)
        np.testing.assert_allclose(s, expected_s)


    def test_calc_q_r(self):
        '''
        This test verifies correct computation of r(x) and q(x)
        assumptions:
        deg(f) = k(2p-1) = 5(2*8-1) = 60, k=5, p=2**3=8
        deg(x**(k*p)) = 40
        '''

        f_x = x**60 + 50*x**50 + 40*x**40  +10*x**10 +5*x**5 + x + 1
        f = sym_to_coeffs(f_x)
        n = len(f) - 1
        k = algo.calc_k(n)
        m = algo.calc_m(n, k)
        p = 2**(m-1)
        print('k=' + str(k) + ', p=' + str(p))
        q, r = algo.calc_q_r(f, k, p)
        print('q,r:')
        print_as_sym(q)
        print_as_sym(r)

        expected_q = sym_to_coeffs(x**20 + 50.0*x**10 + 40.0)
        expected_r = sym_to_coeffs(10.0*x**10 + 5.0*x**5 + 1.0*x + 1.0)
        np.testing.assert_allclose(q, expected_q)
        np.testing.assert_allclose(r, expected_r)


    # def test_sp(self):
    #     f = [1, 2, 3, 4]
    #     u = 5
    #     algo.sp(f, u)


    def test_calc_val(self):
        f_x = x**14 + 2*x**2 + x + 1
        f = sym_to_coeffs(f_x)
        u = 2
        val = algo.calc_val(f, u)
        self.assertEqual(val, np.polyval(f, u))


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

    def test_calc_f_tilde_1(self):
        '''
        assumptions:
        deg(f) =  k(2p-1) = 5(2*4-1) = 35, k=5, p=2**2=4
        :return:
        '''
        k = 5
        p = 2 ** 2
        f = sym_to_coeffs(x**35 + 25*x**25 +20*x**20 +15*x**15 +10*x**10 +5*x**5 + x + 1)
        f_tilde = algo.calc_f_tilde(f, k, p)
        expected_f_tilde = sym_to_coeffs(x**35 + 25*x**25 +20*x**20 +15*x**15 +10*x**10 +5*x**5 + x + 1)
        np.testing.assert_allclose(f_tilde, expected_f_tilde)


    def test_calc_f_tilde_2(self):
        '''
        assumptions:
        deg(f) <  k(2p-1) = 5(2*4-1) = 35, k=5, p=2**2=4
        :return:
        '''
        k = 5
        p = 2 ** 2
        f = sym_to_coeffs(x**30 + 25*x**25 +20*x**20 +15*x**15 +10*x**10 +5*x**5 + x + 1)
        f_tilde = algo.calc_f_tilde(f, k, p)
        expected_f_tilde = sym_to_coeffs(x**35 + x**30 + 25*x**25 +20*x**20 +15*x**15 +10*x**10 +5*x**5 + x + 1)
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


    def test_calc_k_p(self):
        f_x = x ** 14 + 25 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        k, p = algo.calc_k_p(f)
        print('f=' + str(f))
        print('k=' + str(k))
        print('p=' + str(p))

    8

    def test_calc_m(self):
        for n in (2, 100):
            k = algo.calc_k(n)
            m = algo.calc_m(n,k)
            self.assertTrue(k*(2**m-1) > n)
            self.assertTrue(k*(2**(m-1)-1) <= n)

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
