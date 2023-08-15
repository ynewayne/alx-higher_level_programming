# Python - Importing and Modules

This project focuses on the concept of importing functions, using modules, and exploring various Python features. The project also delves into the application of the built-in function `dir()` and the utilization of command-line arguments within Python programs.

## Tasks :page_with_curl:

* **0. Importing a Simple Function from a Simple File**
  * [0-add.py](./0-add.py): This Python program imports the function `def add(a, b):` from [add_0.py](./add_0.py) and displays the result of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a newline.

* **1. My First Toolbox!**
  * [1-calculation.py](./1-calculation.py): This Python program imports functions from [calculator_1.py](./1-calculator.py) and outputs the results of addition, subtraction, multiplication, and division of `10` and `5`.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a newline.

* **2. Making a Script Dynamic!**
  * [2-args.py](./2-args.py): This Python program displays the count and list of its arguments.
  * Output: `[Number of arguments] argument` (if the number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no arguments were passed), followed by
    * A newline, followed by
    * One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another newline.

* **3. Infinite Addition**
  * [3-infinite_add.py](./3-infinite_add.py): This Python program displays the sum of all provided arguments.
  * Output: Sum of the arguments followed by a newline.

* **4. Who Am I?**
  * [4-hidden_discovery.py](./4-hidden_discovery.py): This Python program prints all names defined within the compiled module `hidden_4.pyc`.
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are excluded.

* **5. Import Everything**
  * [5-variable_load.py](./5-variable_load.py): This Python program imports the variable `a` from [variable_load_5.py](./variable_load_5.py) and displays its value.

* **6. Building My Own Calculator!**
  * [100-my_calculator.py](./100-my_calculator.py): This Python program imports functions from [calculator_1.py](./calculator_1.py) to handle basic operations.
  * Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a newline.
  * Output: `<a> <operator> <b> = <result>` followed by a newline.
  * The parameter `operator` can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is not among the above, the program prints `Unknown operator.
  Available operators: +, -, *, and /` followed by a newline and exits with a status value of `1`.
  * If the number of arguments is not three, the program prints `Usage: ./100-my_calculator.py <a> <operator> <b>` followed by a newline and exits with a status value of `1`.

* **7. Easy Print**
  * [101-easy_print.py](./101-easy_print.py): This Python program prints `#pythoniscool` followed by a newline in the standard output.
  * Achieved without using `print`, `eval`, `open`, or `sys`.

* **8. ByteCode -> Python #3**
  * [102-magic_calculation.py](./102-magic_calculation.py): This Python function exactly matches a bytecode provided by Holberton School.

* **9. Swift Alphabet**
  * [103-fast_alphabet.py](./103-fast_alphabet.py): This Python program prints the alphabet in uppercase, followed by a newline.
  * Accomplished without utilizing loops, conditionals, `str.join()`, string literals, or system calls.

