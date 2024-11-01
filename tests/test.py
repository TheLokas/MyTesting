import unittest
from main import find_roots
import math


class TestFindRoots(unittest.TestCase):

    def test_invalid_zero_a(self):
        """Тест, когда коэффициент a равен 0."""
        with self.assertRaises(ValueError):     # Ожидается выброс ValueError
            find_roots(0, 1, 1)                 # Уравнение: 1x + 1 = 0

    def test_two_different_real_roots(self):
        """Тест, когда уравнение имеет два различных действительных корня."""
        root1, root2 = find_roots(1, -3, 2)  # Уравнение: x^2 - 3x + 2 = 0
        self.assertAlmostEqual(root1, 2.0)   # Ожидается, что первый корень равен 2.0
        self.assertAlmostEqual(root2, 1.0)   # Ожидается, что второй корень равен 1.0

    def test_one_double_root(self):
        """Тест, когда уравнение имеет один действительный корень."""
        root1, root2 = find_roots(1, -2, 1)  # Уравнение: x^2 - 2x + 1 = 0
        self.assertAlmostEqual(root1, 1.0)   # Ожидается, что оба корня равны 1.0
        self.assertAlmostEqual(root2, 1.0)

    def test_no_real_roots(self):
        """Тест, когда уравнение имеет отрицательный дискриминант (нет действительных корней)."""
        root1, root2 = find_roots(1, 1, 1)   # Уравнение: x^2 + x + 1 = 0
        self.assertIsNone(root1)              # Ожидается, что корни равны None
        self.assertIsNone(root2)

    def test_c_zero_positive_discriminant(self):
        """Тест, когда коэффициент с равен 0."""
        root1, root2 = find_roots(1, 2, 0)    # Уравнение: x^2 + 2x = 0
        self.assertAlmostEqual(root1, 0.0)      # Ожидается, что первый корень равен 0.0
        self.assertAlmostEqual(root2, -2.0)     # Ожидается, что второй корень равен -2.0

    def test_b_zero_positive_discriminant(self):
        """Тест, когда коэффициент b равен 0. """
        root1, root2 = find_roots(1, 0, -4)   # Уравнение: x^2 - 4 = 0
        self.assertAlmostEqual(root1, 2.0)     # Ожидается, что первый корень равен 2.0
        self.assertAlmostEqual(root2, -2.0)    # Ожидается, что второй корень равен -2.0



if __name__ == '__main__':
    unittest.main()
