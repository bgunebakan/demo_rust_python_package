import pytest

from demo_rust_python_package import (
    Calculator,
    word_count,
    reverse_string,
)


class TestCalculator:

    def setup_method(self):
        self.calc = Calculator("TestCalc")

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0

    def test_multiply(self):
        assert self.calc.multiply(4, 5) == 20
        assert self.calc.multiply(-2, 3) == -6

    def test_sum_list(self):
        assert self.calc.sum_list([1, 2, 3, 4, 5]) == 15
        assert self.calc.sum_list([]) == 0
        assert self.calc.sum_list([-1, 1]) == 0
        assert self.calc.sum_list([1.5, 2.5]) == 4.0

    def test_word_count(self):
        assert word_count("This is a test.") == 4

    def test_reverse_string(self):
        assert reverse_string("Hello World!") == "!dlroW olleH"


if __name__ == "__main__":
    pytest.main([__file__])
