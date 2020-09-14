import unittest
from crt_tools import *


class Tests(unittest.TestCase):

    def test_prod_hat(self):
        self.assertEqual(calc_prod_hat([2, 3, 5], 0), 15)
        self.assertEqual(calc_prod_hat([2, 3, 5], 1), 10)
        self.assertEqual(calc_prod_hat([2, 3, 5], 2), 6)

    def test_gcd(self):
        gcd, x ,y = gcdExtended(2, 3)
        self.assertEqual(1, gcd)
        self.assertEqual(-1, x)
        self.assertEqual(1, y)

    def test_inverse(self):
        self.assertEqual(4, inverse(4, 5))

    def test_get_int(self):
        self.assertEqual(100 % (2*3*5*7), get_int([0,1,0,2], [2,3,5,7]))
        self.assertEqual(100 % (2*3*5), get_int([0,1,0], [2,3,5]))

    def test_transform_basis(self):
        self.assertEqual([0, 1, 0, 3], transform_basis([0,1,0], [2,3,5], [2,3,5,7]))


if __name__ == '__main__':
    unittest.main()
