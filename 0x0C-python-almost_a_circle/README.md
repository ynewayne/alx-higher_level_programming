

This project showcases my proficiency in Python object-oriented programming, as demonstrated through the implementation of three interconnected classes representing rectangles and squares. To ensure the robustness of the code, I developed a comprehensive test suite using the `unittest` module, covering all functionalities of each class.

The implementation of these classes involved the utilization of various Python tools, including:

- Import statements
- Exception handling
- Private attributes
- Getter and setter methods
- Class and static methods
- Inheritance
- File I/O operations
- Use of `args` and `kwargs`
- JSON and CSV serialization/deserialization
- Unit testing

## Tests :heavy_check_mark:

- [tests/test_models](./tests/test_models): This directory contains independently developed test files for each class:
  - [test_base.py](./tests/test_models/test_base.py)
  - [test_rectangle.py](./tests/test_models/test_rectangle.py)
  - [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
This serves as the base class for all other classes in the project, offering the following features:

- Private class attribute `__nb_objects = 0`.
- Public instance attribute `id`.
- Class constructor `def __init__(self, id=None):`
  - If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  - Otherwise, sets the public instance attribute `id` to the provided `id`.
- Static method `def to_json_string(list_dictionaries):` that returns the JSON string serialization of a list of dictionaries.
  - Returns `"[]"` if `list_dictionaries` is `None` or empty.
- Class method `def save_to_file(cls, list_objs):` that writes the JSON serialization of a list of objects to a file.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`).
  - Overwrites the file if it already exists.
- Static method `def from_json_string(json_string):` that returns a list of objects deserialized from a JSON string.
  - Returns an empty list if `json_string` is `None` or empty.
- Class method `def create(cls, **dictionary):` that instantiates an object with provided attributes.
  - Instantiates an object with the attributes given in `**dictionary`.
- Class method `def load_from_file(cls):` that returns a list of objects instantiated from a JSON file.
  - Reads from the JSON file `<cls name>.json` (e.g., `Rectangle.json`).
  - Returns an empty list if the file does not exist.
- Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV serialization of a list of objects to a file.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.csv` (e.g., `Rectangle.csv`).
  - Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
- Class method `def load_from_file_csv(cls):` that returns a list of objects instantiated from a CSV file.
  - Reads from the CSV file `<cls name>.csv` (e.g., `Rectangle.csv`).
  - Returns an empty list if the file does not exist.
- Static method `def draw(list_rectangles, list_squares):` that draws `Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  - The parameter `list_rectangles` is expected to be a list of `Rectangle` objects to print.
  - The parameter `list_squares` is expected to be a list of `Square` objects to print.

### Rectangle

This class represents a rectangle and inherits from `Base`. It includes:

- Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  - Each private instance attribute features its own getter/setter.
- Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  - Raises a `TypeError` exception with the message `<attribute> must be an integer` if either of `width`, `height`, `x`, or `y` is not an integer.
  - Raises a `ValueError` exception with the message `<attribute> must be > 0` if either `width` or `height` is >= 0.
  - Raises a `ValueError` exception with the message `<attribute> must be >= 0` if either `x` or `y` is less than 0.
- Public method `def area(self):` that returns the area of the `Rectangle` instance.
- Public method `def display(self):` that prints the `Rectangle` instance to `stdout` using the `#` character.
  - Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
- Overwrite of `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` that updates an instance of a `Rectangle` with the given attributes.
  - `*args` must be supplied in the following order:
    - 1st: `id`
    - 2nd: `width`
    - 3rd: `height`
    - 4th: `x`
    - 5th: `y`
  - `**kwargs` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
  - `**kwargs` is skipped if `*args` exists.
- Public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle` instance.

### Square

This class represents a square and inherits from `Rectangle`:

- Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  - The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
- Overwrite of `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
  - `*args` must be supplied in the following order:
    - 1st: `id`
    - 2nd: `size`
    - 3rd: `x`
    - 4th: `y`
  - `**kwargs` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Square` with.
  - `**kwargs` is skipped if `*args` exists.
- Public method `def to_dictionary(self):
