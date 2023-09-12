# Python - Learning Inheritance

In this project, I gained knowledge about the concept of inheritance in Python. I acquired insights into various aspects of inheritance, including working with super- and sub-classes, defining classes with multiple base classes, and overriding inherited methods and attributes.

## Testing :heavy_check_mark:

* [tests](./tests): This directory contains test files:
    * [1-my_list.txt](./1-my_list.txt)
    * [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Below are the function prototypes for the functions implemented in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Tasks :page_with_curl:

* **0. Lookup**
  * [0-lookup.py](./0-lookup.py): This Python function returns a list of available attributes and methods of an object.

* **1. My list**
  * [1-my_list.py](./1-my_list.py): I implemented a Python class called `MyList`, which inherits from the built-in `list` class. This class includes a public instance method named `def print_sorted(self)` that prints the list in ascending sorted order, assuming all list elements are integers.

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py): I created a Python function that determines whether an object is exactly an instance of a specified class. It returns `True` if the object is an instance of the specified class and `False` otherwise.

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): In this task, I implemented a Python function that checks if an object is an instance of a specified class or inherits from it. It returns `True` if the object is an instance or an inherited instance of the specified class; otherwise, it returns `False`.

* **4. Only sub class of**
  * [4-inherits_from.py](./4-inherits_from.py): I created a Python function that determines if an object is an inherited instance, either directly or indirectly, from a specified class. It returns `True` if the object is an inherited instance; otherwise, it returns `False`.

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py): I defined an empty Python class called `BaseGeometry`.

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py): I expanded on the previous task by enhancing the `BaseGeometry` class. This class includes a public instance method named `def area(self)` that raises an `Exception` with the message "area() is not implemented."

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry.py): In this task, I further improved the `BaseGeometry` class by adding a public instance method named `def integer_validator(self, name, value)`. This method validates the parameter `value`, assuming that the parameter `name` is always a string. The method ensures that `value` is an integer and greater than 0. If the validation fails, it raises exceptions accordingly.

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py): I implemented a Python class called `Rectangle`, which inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). This class includes private attributes `width` and `height`, both validated with the `integer_validator` method. The class also includes instantiation with `width` and `height`.

* **9. Full rectangle**
  * [9-rectangle.py](./9-rectangle.py): I continued to work on the `Rectangle` class ([8-rectangle.py](./8-rectangle.py)) by implementing the `area()` method. I also added a special method `__str__` to print rectangles in the format "[Rectangle] \<width>/\<height>".

* **10. Square #1**
  * [10-square.py](./10-square.py): I created a Python class called `Square`, which inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). This class includes a private attribute `size`, validated with the `integer_validator` method. The class allows instantiation with `size` and implements the `area()` method.

* **11. Square #2**
  * [11-square.py](./11-square.py): In this task, I extended the `Square` class ([10-square.py](./10-square.py)) by adding a special method `__str__` to print squares in the format "[Square] \<width>/\<height>".

* **12. My integer**
  * [100-my_int.py](./100-my_int.py): I created a Python class called `MyInt`, which inherits from the built-in `int` class. This class inverts the behavior of the `==` and `!=` operators.

* **13. Can I?**
  * [101-add_attribute.py](./101-add_attribute.py): I implemented a Python function that adds a new attribute to an object if it is possible to do so. If adding the attribute is not possible, the function raises a `TypeError` exception with the message "can't add new attribute."
 
