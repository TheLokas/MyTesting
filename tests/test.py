import unittest
from main import find_roots
import math


class TestFindRoots(unittest.TestCase):

    def test_two_real_roots(self):
        """Тест, когда уравнение имеет два различных действительных корня"""
        a, b, c = 1, -3, 2
        roots = find_roots(a, b, c)
        self.assertIsNotNone(roots)
        self.assertNotEqual(roots[0], roots[1])
        self.assertAlmostEqual(roots[0] * roots[1], c / a, delta=1e-9)
        self.assertAlmostEqual(roots[0] + roots[1], -b / a, delta=1e-9)

    def test_one_real_root(self):
        """Тест, когда уравнение имеет один действительный корень"""
        a, b, c = 1, 0, 1
        roots = find_roots(a, b, c)
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 2)
        self.assertEqual(roots[0], roots[1])
        if roots[0] is not None:
            self.assertAlmostEqual(roots[0] ** 2 + b * roots[0] + c, 0, places=6)
        else:
            self.assertIsNone(roots[0])
            self.assertIsNone(roots[1])

    def test_integer_coefficients(self):
        """Тест, когда коэффициенты a, b, c - целые числа"""
        a, b, c = 1, -2, 1
        roots = find_roots(a, b, c)
        self.assertIsNotNone(roots)
        self.assertEqual(roots[0], roots[1])
        self.assertAlmostEqual(roots[0] ** 2 + b * roots[0] + c, 0, delta=1e-9)

    def test_float_coefficients(self):
        """Тест, когда коэффициенты a, b, c - вещественные числа"""
        a, b, c = 1.5, 2.3, -1.0
        roots = find_roots(a, b, c)

        self.assertTrue(math.isclose(roots[0] ** 2 + b * roots[0] + c, 0, rel_tol=1e-5))
        self.assertTrue(math.isclose(roots[1] ** 2 + b * roots[1] + c, 0, rel_tol=1e-5))

    def test_negative_discriminant(self):
        """Тест, когда дискриминант отрицательный (нет действительных корней)"""
        a, b, c = 1, 1, 1
        roots = find_roots(a, b, c)
        self.assertIsNotNone(roots)
        self.assertIsNone(roots[0])
        self.assertIsNone(roots[1])

    def test_all_zero_coefficients(self):
        """Тест, когда все коэффициенты равны 0"""
        a, b, c = 0, 0, 0
        with self.assertRaises(ValueError):
            find_roots(a, b, c)


if __name__ == '__main__':
    unittest.main()