import pytest

from pipeline_test.math_package import add_function, subtract_function

class TestClass:
    def test_one_plus_one_is_three(self):
        assert add_function(1, 2) == 3

    def test_two_plus_two_is_four(self):
        assert add_function(2, 2) == 4

    def test_one_minus_two_is_negative_one(self):
        assert subtract_function(1, 2) == -1

    def test_two_minus_two_is_zero(self):
        assert subtract_function(2, 2) == 0