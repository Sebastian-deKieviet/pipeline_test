import pytest

from pipeline_test.sample_package import sample_function

class TestClass:
    def test_one(self):
        assert sample_function(1, 2) == 3

    def test_two(self):
        assert sample_function(2, 2) == 4