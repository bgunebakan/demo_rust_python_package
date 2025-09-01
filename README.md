# Demo Rust Python Package

## Installation

### Prerequisites

- Python 3.8+
- Rust
- Maturin

### Building

```bash

maturin develop

```

## Usage

### Basic Calculator Operations

```python
from demo_rust_python_package import Calculator

calc = Calculator("MyCalculator")

result = calc.add(10, 20)
result = calc.multiply(5, 6)

numbers = [1, 2, 3, 4, 5]
total = calc.sum_list(numbers)
```

### Standalone Functions

```python
from demo_rust_python_package import word_count, reverse_string

text = "Hello, Rust and Python integration!"
word_count = word_count(text)

reversed_text = reverse_string(text)
```
