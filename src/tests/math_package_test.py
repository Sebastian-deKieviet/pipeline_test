import pytest

from pipeline_test.math_package import add_function, subtract_function

class TestClass:
    def test_one(self):
        assert add_function(1, 2) == 3

    def test_two(self):
        assert add_function(2, 2) == 4

    def test_three(self):
        assert subtract_function(1, 2) == -1

    def test_four(self):
        assert add_function(2, 2) == 0