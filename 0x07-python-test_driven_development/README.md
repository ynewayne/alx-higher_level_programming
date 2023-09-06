This directory contains the files required to complete the 0x07. Python - Test-driven developmenttask in ALX. The scripts and their fucntions are listed below.

Here's a paraphrased version of the readme:

**Python - Test-driven development**

This project focuses on practicing test-driven development in Python using `docstring` and `unittest`.

## Tests :heavy_check_mark:

* [tests](./tests): Contains test files, including both those provided by Holberton and independently-developed ones:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

Function prototypes for this project are as follows:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

## Tasks :page_with_curl:

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): A Python function that returns the integer addition of two numbers.
  * Handles cases where either `a` or `b` is not an `int` or `float`, raising a `TypeError` with the appropriate message.
  * Casts `float` values to `int` before addition.

* **1. Divide a matrix**
  * [2-matrix_divided.py](./2-matrix_divided.py): A Python function that divides all elements of a matrix by a common divisor.
  * Returns a new matrix with rounded quotients.
  * Handles various error cases, including checking the data types of input and division by zero.

* **2. Say my name**
  * [3-say_my_name.py](./3-say_my_name.py): A Python function that prints a name in the format `My name is <first_name> <last_name>`.
  * Checks the data types of `first_name` and `last_name` and raises a `TypeError` if they are not strings.

* **3. Print square**
  * [4-print_square.py](./4-print_square.py): A Python function that prints a square using the `#` character.
  * Validates the input `size` and handles error cases.

* **4. Text indentation**
  * [5-text_indentation.py](./5-text_indentation.py): A Python function that prints text with specific indentation rules.
  * Ensures that the input `text` is a string and maintains proper indentation.

* **5. Max integer - Unittest**
  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): A Python class/script that runs unittests for the `max_integer` function.

* **6. Matrix multiplication**
  * [100-matrix_mul.py](./100-matrix_mul.py): A Python function that multiplies two matrices.
  * Handles various error cases related to input validation and matrix compatibility.

* **7. Lazy matrix multiplication**
  * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): A Python function that multiplies two matrices using the `NumPy` module.
  * Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).

* **8. CPython #3: Python Strings**
  * [102-python.c](./102-python.c): A C function that prints basic information about Python string objects.

This paraphrased version retains the original content but presents it in a more concise and readable manner.
