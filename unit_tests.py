import unittest
import paterson_stockmeyer_algo as algo
from test_utils import *


class Tests(unittest.TestCase):

    def test_ps(self):
        f_x = x ** 20 + 15 * x ** 15 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        u = 5
        val = algo.ps(f, u)
        self.assertEqual(val, np.polyval(f, u))

    def test_calc_c_s(self):
        '''
        this test verifies:
        1) correct computation of s(x) and c(x)
        2) s(x) + x**[k(p-1)] is monic with degree k(p-1)
        3) deg(c) <= k -1

        '''
        f_x = x ** 20 + 15 * x ** 15 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        k, p, _ = algo.calc_k_p_m(f)
        f_tilde = algo.calc_f_tilde(f, k, p)
        q = sym_to_coeffs(x**9 + x**8 + 15.*x**3)
        r = sym_to_coeffs(10 * x ** 10 + 5 * x ** 5 + x + 1)
        c, s = algo.calc_c_s(r, q, k, p)
        expected_c = sym_to_coeffs(10 * x - 11)
        expected_s = sym_to_coeffs(11*x**8 + 5*x**5 - 150*x**4 + 165*x**3 + x + 1.0)
        np.testing.assert_allclose(c, expected_c)
        np.testing.assert_allclose(s, expected_s)

    def test_calc_q_r(self):
        f_x = x ** 20 + 15 * x ** 15 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        k, p, m = algo.calc_k_p_m(f)
        f_tilde = algo.calc_f_tilde(f, k, p)
        q, r = algo.calc_q_r(f_tilde, k, p)
        expected_q = sym_to_coeffs(x**9 + x**8 + 15.*x**3)
        expected_r = sym_to_coeffs(10 * x ** 10 + 5 * x ** 5 + x + 1)
        np.testing.assert_allclose(q, expected_q)
        np.testing.assert_allclose(r, expected_r)

    def test_ps_586(self):
        f = [4, 3, 2, 1]
        u = 5
        self.assertEqual(algo.ps(f, u),586)

    def test_evaluate_c(self):
        f_x = x ** 20 + 15 * x ** 15 + 10 * x ** 10 + 5 * x ** 5 + x + 1
        f = sym_to_coeffs(f_x)
        k, p, m = algo.calc_k_p_m(f)
        f_tilde = algo.calc_f_tilde(f, k, p)
        q, r = algo.calc_q_r(f_tilde, k, p)
        c, s = algo.calc_c_s(r, q, k, p)
        u = 5
        val = algo.evaluate_deg_less_than_k(c, u, k, p, algo.precomputed_u_powers_less_than_k(u, k))
        self.assertEqual(val, np.polyval(c, u))

    def test_calc_f_tilde(self):
        f = sym_to_coeffs(x**20 + 15*x**15 +10*x**10 +5*x**5 + x + 1)
        k, p, _ = algo.calc_k_p_m(f)
        f_tilde = algo.calc_f_tilde(f, k, p)
        expected_f_tilde = sym_to_coeffs(x**21 + x**20 + 15*x**15 + 10*x**10 + 5*x**5 + x + 1.0)
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
        k, p, m = algo.calc_k_p_m(f)

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
