from .demo_rust_python_package import Calculator, word_count, reverse_string

__version__ = "0.1.0"
__all__ = [
    "Calculator",
    "CustomCalculator",
    "word_count",
    "reverse_string",
]


class CustomCalculator:
    """
    A Python class that wraps the Rust Calculator and adds additional functionality.
    """

    def __init__(self, name: str = "MyPreciousCalculator"):
        self._calculator = Calculator(name)

    def add(self, a: float, b: float) -> float:
        print(f"Adding {a} and {b}")
        return self._calculator.add(a, b)

    def multiply(self, a: float, b: float) -> float:
        print(f"Multiplying {a} and {b}")
        return self._calculator.multiply(a, b)

    def sum_list(self, numbers: list) -> float:
        print(f"Summing list: {numbers}")
        return self._calculator.sum_list(numbers)
