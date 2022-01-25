import unittest
from sympy.abc import *
from sympy import *
from sympytools.extension import *


class TestExtensions(unittest.TestCase):

    def test_factor_out(self):
        expr = -2 * exp(I * delta * j * k) + exp(I * delta * k * (j - 1)) + exp(I * delta * k * (j + 1))
        actual = factor_out(expr, exp(I*delta*j*k))
        expected = (-2 + exp(-I * delta * k) + exp(I * delta * k )) * exp(I * delta * j * k)
        self.assertEqual(expected, actual)


class TestLineIntegral(unittest.TestCase):

    def test_lineintegral_xy(self):
        circle = Path('C',
              {x: cos(t),
               y: sin(t)},
              (t, 0, 2*pi))

        actual = LineIntegral(2 * y, x, circle) - LineIntegral(3 * x, y, circle)
        self.assertEqual(-5*pi, actual.doit())

    def test_lineintegral_complex(self):
        circle = Path('C',
                      {x: cos(t),
                       y: sin(t)},
                      (t, 0, 2 * pi))
        f = (1 / z).subs(z, x + I * y)
        actual = LineIntegral(f, x, circle) + I * LineIntegral(f, y, circle)
        self.assertEqual(2*pi*I, actual.doit())

    def test_contourintegral(self):
        circle = Path('C',
                      {z: exp(I*theta)},
                      (theta, 0, 2 * pi))
        actual = ContourIntegral(1/z, z, circle)
        self.assertEqual(2*pi*I, actual.doit())


if __name__ == '__main__':
    unittest.main()
