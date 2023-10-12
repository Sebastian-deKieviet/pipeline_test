import pytest

from pipeline_test.math_package import add_function, subtract_function

class TestClass:
    def test_one_plus_one_is_three(self):
        '''Verifies that the add_function returns 3, when the input is 1 and 2'''
        assert add_function(1, 2) == 3

    def test_two_plus_two_is_four(self):
        '''Verifies that the add_function returns 4, when the input is 2 and 2'''
        assert add_function(2, 2) == 4

    def test_one_minus_two_is_negative_one(self):
        '''Verifies that the subtract_function returns -1, when the input is 1 and 2'''
        assert subtract_function(1, 2) == -1

    def test_two_minus_two_is_zero(self):
        '''Verifies that the subtract_function returns 0, when the input is 2 and 2'''
        assert subtract_function(2, 2) == 0