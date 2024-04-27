import unittest

from src.lab1.calculator import *


class CalculatorTestCase(unittest.TestCase):
    def test_Calculator(self):
        #addition_test
        self.assertEqual(calculator(5, 20, '+'), 25)
        self.assertEqual(calculator(5, -90, '+'), -85)
        self.assertEqual(calculator(5, 0, '+'), 5)
        self.assertAlmostEqual(calculator(0.01, 0.003, '+'), 0.013)
        self.assertAlmostEqual(calculator(0.01, -0.003, '+'), 0.007)

        #substraction_test
        self.assertEqual(calculator(5, 5, '-'), 0)
        self.assertEqual(calculator(-31, -6, '-'), -25)
        self.assertEqual(calculator(-31, 6, '-'), -37)
        self.assertEqual(calculator(-5, 0, '-'), -5)
        self.assertEqual(calculator(3, 0, '-'), 3)
        self.assertAlmostEqual(calculator(0.01, 0.003, '-'), 0.007)

        #multiplication test
        self.assertEqual(calculator(3, 3, '*'), 9)
        self.assertEqual(calculator(-5, 3, '*'), -15)
        self.assertEqual(calculator(-5, -3, '*'), 15)
        self.assertEqual(calculator(4, 0, '*'), 0)
        self.assertAlmostEqual(calculator(0.2, 0.008, '*'), 0.0016)
        self.assertAlmostEqual(calculator(0, 0.008, '*'), 0)

        #division test
        self.assertEqual(calculator(10, 2, '/'), 5)
        self.assertEqual(calculator(6, -2, '/'), -3)
        self.assertEqual(calculator(-6, -2, '/'), 3)
        self.assertEqual(calculator(5, 1, '/'), 5)
        self.assertEqual(calculator(0, 7, '/'), 0)
        self.assertRaises(ZeroDivisionError, calculator, 7, 0, '/')
        self.assertAlmostEqual(calculator(0.04, 0.2, '/'), 0.2)
        self.assertAlmostEqual(calculator(0, 0.006, '/'), 0)


if __name__ == '__main__':
    unittest.main()