"README.md
# Python - Further Exploration of Classes and Objects

In this project, I continued to delve into the realm of object-oriented programming in Python. My journey involved mastering concepts such as class methods, static methods, class vs. instance attributes, and harnessing the power of the `__str__` and `__repr__` special methods.

## Tests :heavy_check_mark:

* [tests](./tests): This directory contains a collection of test files thoughtfully provided by Holberton School.

## Tasks :page_with_curl:

* **0. Simple rectangle**
  * [0-rectangle.py](./0-rectangle.py): An elementary Python class is born, defining the essence of a rectangle. (Spoiler alert: It's empty!)

* **1. The true form of a rectangle**
  * [1-rectangle.py](./1-rectangle.py): This Python class elevates the definition of a rectangle by endowing it with:
    * A private instance attribute named `width`.
    * A property getter `def width(self):` that retrieves the `width`.
    * A property setter `def width(self, value):` that sets the `width`.
    * Another private instance attribute named `height`.
    * A property getter `def height(self):` that retrieves the `height`.
    * A property setter `def height(self, value):` that sets the `height`.
    * The class constructor `def __init(self,   width=0, height=0):`, allowing for instantiating rectangles with optional `width` and `height`.
  * In case `width` or `height` is not an integer, a `TypeError` swiftly intervenes with the message `width must be an integer` or `height must be an integer`.
  * And if `width` or `height` dare to be less than zero, a `ValueError` chimes in with `width must be >= 0` or `height must be >= 0`.

* **2. Area and Perimeter**
  * [2-rectangle.py](./2-rectangle.py): This Python class, a product of refinement, includes:
    * A public instance method `def area(self):` for calculating the area of the rectangle.
    * A public instance attribute `def perimeter(self):` for computing the perimeter of the rectangle (unless `width` or `height` is zero, in which case, the perimeter is zero).

* **3. String representation**
  * [3-rectangle.py](./3-rectangle.py): In this evolution of our Python class, we introduce a special method `__str__` that crafts a visual representation of the rectangle using the `#` character. If `width` or `height` is zero, it gracefully returns an empty string.

* **4. Eval is magic**
  * [4-rectangle.py](./4-rectangle.py): As our Python class matures, it gains a new ability with the addition of the special method `__repr__`, which bestows upon it the power to return a string representation fit for official purposes.

* **5. Detect instance deletion**
  * [5-rectangle.py](./5-rectangle.py): This Python class reaches a level of self-awareness with the introduction of the special method `__del__`, which kindly announces its departure with the message `Bye rectangle...` when a `Rectangle` is deleted.

* **6. How many instances**
  * [6-rectangle.py](./6-rectangle.py): Our Python class now possesses a public class attribute `number_of_instances`, starting at zero and diligently incrementing with each new instantiation. It also decreases when instances are deleted.

* **7. Change representation**
  * [7-rectangle.py](./7-rectangle.py): A new customization feature arrives, bringing with it a public class attribute `class_symbol`. By default, it's set to `#`, but it's open to change - it defines the symbol used for the string representation of our rectangle.

* **8. Compare rectangles**
  * [8-rectangle.py](./8-rectangle.py): A versatile Python class emerges with a static method `def bigger_or_equal(rect_1, rect_2):`, which assists in determining the rectangle with the greater area (or simply returns `rect_1` if both areas are equal). Should either `rect_1` or `rect_2` fail to be a `Rectangle` instance, a `TypeError` issues a stern warning with the message `rect_1 must be an instance of Rectangle` or `rect_2 must be an instance of Rectangle`.

* **9. A square is a rectangle**
  * [9-rectangle.py](./9-rectangle.py): The class method `def square(cls, size=0):` makes its debut, returning a fresh `Rectangle` instance with both `width` and `height` set to `size`. It's a special moment when a square is recognized as a rectangle!

* **10. N Queens**
  * [101-nqueens.py](./101-nqueens.py): Behold, a Python program of grandeur! It tackles the age-old [N queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) with grace. You can invoke its wisdom with `./101-n

queens.py N`.
  * It explores all conceivable solutions for placing N non-attacking queens on an NxN chessboard.
  * The program stands firm on expecting exactly two arguments; otherwise, it politely guides you with `Usage: nqueens N` and exits respectfully with a status of `1`.
  * If you dare provide an `N` that is not an integer, it gently admonishes with `N must be a number` and exits with the same respectful status.
  * And if, in your ambition, you set `N` less than `4`, it calmly asserts `N must be at least 4` and departs in a dignified manner.
  * In the end, it presents its solutions, one per line, in the format `[[r, c], [r, c], [r, c], [r, c]]`, where `r` and `c` denote the row and column, respectively, where a queen shall reign supreme."


