#!/usr/bin/env python3
from demo_rust_python_package import (
    Calculator,
    CustomCalculator,
    word_count,
    reverse_string,
)


def main():

    print("Basic Operations:")
    calc = Calculator("MyCalculator")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"7 * 8 = {calc.multiply(7, 8)}")
    print(f"Sum of [10, 20, 30] = {calc.sum_list([10, 20, 30])}")

    print("\nPython Wrapper:")
    my_calc = CustomCalculator("MyCalculator")
    print(my_calc.add(1, 2))
    print(my_calc.multiply(3, 4))
    print(my_calc.sum_list([1, 2, 3, 4, 5]))

    print("\nStandalone Functions:")
    text = "Hello World!"
    print(f"Original: '{text}'")
    print(f"Word count: {word_count(text)}")
    print(f"Reversed: '{reverse_string(text)}'")


if __name__ == "__main__":
    main()
