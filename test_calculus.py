"""
Unit testing module for testing functions in calculus.py
"""

import unittest # Import the unittest module
import numpy as np
import calculus as calc

class TestCalculusFunctions(unittest.TestCase):
    """
    Unit tests for integration-related functions.

    This class tests the correctness and accuracy of functions related to
    numerical and symbolic integration. It includes tests for definite and
    indefinite integrals, handling of improper integrals, edge cases, and
    the behavior of integration functions for a variety of mathematical
    expressions and domains.
    """
    def test_simpson(self): # Indent this function definition
        """Test the simpson function with a known integral."""
# Function: x^3 + 1
        def f(x):
            return x**3 + 1

        # Initial guesses and expected outcome for Function: x^3 + 1
        a = -1
        b = 1
        n = 100
        expected_integral = 2

        # Call the simpson function from calculus module
        result = calc.simpson(f, a, b, n)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=5)

    # Indent the following functions one level further to be part of the class
    def exp_minus_1_over_x(self, x): # Added 'self' as argument for class methods
        """f: e^(-1/x)"""
        return np.exp(-1/x)

    def cos_1_over_x(self, x): # Added 'self' as argument for class methods
        """f: cos(1/x)"""
        return np.cos(1/x)

    def x3_plus_1(self, x): # Added 'self' as argument for class methods
        """f: x^3 + 1"""
        return x**3 + 1

def test_dummy():
    """ 
    Unit test for dummy function
    """
    assert calc.dummy() == 0

def test_trapezoid_numpy():
    '''
    Unit test for numpy implementation of trapezoid method
    '''
    assert np.isclose(calc.trapezoid_numpy(np.sin, 0, np.pi), 2)

def test_trapezoid_scipy():
    '''
    Unit test for scipy implementation of trapezoid method
    '''
    assert np.isclose(calc.trapezoid_scipy(np.sin, 0, np.pi), 2)
