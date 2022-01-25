import unittest

from sympy.abc import *
from sympy import *
from sympytools.mods import *


class TestEquation(unittest.TestCase):

    def test_add_right_to_equation(self):
        eq = Eq(a + b, c)
        actual = eq + d
        self.assertEqual(actual, Eq(a+b+d, c+d))

    def test_add_left_to_equation(self):
        eq = Eq(a + b, c)
        actual = d + eq
        self.assertEqual(actual, Eq(d+a+b, d+c))

    def test_sub_right_to_equation(self):
        eq = Eq(a + b, c)
        actual = eq - d
        self.assertEqual(actual, Eq(a+b-d, c-d))

    def test_sub_left_to_equation(self):
        eq = Eq(a + b, c)
        actual = -d + eq
        self.assertEqual(Eq(-d+a+b, -d+c), actual)

    def test_mul_right_to_equation(self):
        eq = Eq(a + b, c)
        actual = eq * d
        self.assertEqual(Eq((a+b)*d, c*d), actual)

    def test_mul_left_to_equation(self):
        eq = Eq(a + b, c)
        actual = d * eq
        self.assertEqual(Eq(d*(a+b), d*c), actual)

    def test_div_right_to_equation(self):
        eq = Eq(a + b, c)
        actual = eq / d
        self.assertEqual(Eq((a+b)/d, c/d), actual)

    def test_div_left_to_equation(self):
        eq = Eq(a + b, c)
        actual = d / eq
        self.assertEqual(Eq(d/(a+b), d/c), actual)

    def test_add_two_equations(self):
        eq1 = Eq(a, b)
        eq2 = Eq(c, d)
        actual = eq1 + eq2
        expected = Eq(a+c, b+d)
        self.assertEqual(expected, actual)

    def test_sub_two_equations(self):
        eq1 = Eq(a, b)
        eq2 = Eq(c, d)
        actual = eq1 - eq2
        expected = Eq(a-c, b-d)
        self.assertEqual(expected, actual)

    def test_mul_two_equations(self):
        eq1 = Eq(a, b)
        eq2 = Eq(c, d)
        actual = eq1 * eq2
        expected = Eq(a*c, b*d)
        self.assertEqual(expected, actual)

    def test_div_two_equations(self):
        eq1 = Eq(a, b)
        eq2 = Eq(c, d)
        actual = eq1 / eq2
        expected = Eq(a/c, b/d)
        self.assertEqual(expected, actual)

    def test_raise_equation_to_power(self):
        eq = Eq(a, b)
        actual = eq ** 2
        expected = Eq(eq.lhs**2, eq.rhs**2)
        self.assertEqual(expected, actual)

    def test_sqrt_of_equation(self):
        eq = Eq(x, 4)
        actual = sqrt(eq)
        expected = Eq(sqrt(x), 2)
        self.assertEqual(expected, actual)

    def test_atan_of_equation(self):
        eq = Eq(x, 4)
        actual = atan(eq)
        expected = Eq(atan(x), atan(4))
        self.assertEqual(expected, actual)

    def test_apply_rhs_side_only(self):
        eq = Eq((x+y)**2, (a+b)**2)
        actual = eq.apply('rhs', expand)
        expected = Eq((x + y)**2, a**2 + 2*a*b + b**2)
        self.assertEqual(expected, actual)

    def test_apply_lhs_side_only(self):
        eq = Eq((x+y)**2, (a+b)**2)
        actual = eq.apply('lhs', expand)
        expected = Eq(x**2 + 2*x*y + y**2, (a + b)**2)
        self.assertEqual(expected, actual)

    def test_apply_exp_to_both_sides(self):
        eq = Eq(x, 2)
        actual = eq.apply('both', exp)
        expected = Eq(exp(x), exp(2))
        self.assertEqual(expected, actual)

    def test_wrapped_sympy_functions_on_eq(self):
        x, y = symbols('x, y', real=True)
        eq = Eq(x+I, 3+ 2*I*y)
        actual = im(eq)
        expected = Eq(1, 2*y)
        self.assertEqual(expected, actual)

    def test_re_on_equation(self):
        x, y = symbols('x, y', real=True)
        eq = Eq(x, y + 5)
        actual = sqrt(eq)
        expected = Eq(sqrt(x), sqrt(y+5))
        self.assertEqual(expected, actual)

