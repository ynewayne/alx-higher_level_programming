# Python - Input and Output

In this project, I practiced working with file input and output in Python. I utilized built-in functions like `with`, `open`, and `read`, and leveraged the `json` module for reading and writing files. Additionally, I explored the serialization and deserialization of objects using JSON.

## Function Prototypes :floppy_disk:

Below are the prototypes for the functions implemented in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-number_of_lines.py` | `def number_of_lines(filename=""):` |
| `2-read_lines.py` | `def read_lines(filename="", nb_lines=0):` |
| `3-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): This Python function reads and prints the contents of a UTF8 text file to the standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): In this task, I created a Python function that writes a string to a UTF8 text file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): I implemented a Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): In this task, I developed a Python function that returns the JSON string representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): I created a Python function that returns the Python object represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): I implemented a Python function that writes an object to a text file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): In this task, I created a Python function that creates an object from a `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): This Python script stores all command-line arguments into a Python list, which is saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): I developed a Python function that returns the dictionary description for simple Python data structures, including lists, dictionaries, strings, integers, and booleans.

* **9. Student to JSON**
  * [9-student.py](./9-student.py): I created a Python class called `Student` that defines a student. This class includes public instance attributes `first_name`, `last_name`, and `age`. It allows instantiation with these attributes and has a public method `def to_json(self)` that returns the dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): In this task, I enhanced the `Student` class ([11-student.py](./11-student.py)) by adding a public method `def to_json(self, attrs=None)` that returns the dictionary representation of a `Student` instance. If `attrs` is a list of strings, only the attributes listed are represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): I further improved the `Student` class by adding a public method `def reload_from_json(self, json)` that replaces all attributes of the `Student` instance using the key/value pairs listed in `json`. The method assumes that `json` is a dictionary containing attributes with names/values corresponding to key/value pairs.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12

-pascal_triangle.py): In this task, I implemented a Python function that returns a list of lists of integers representing Pascal's triangle of size `n`. The function assumes that the size parameter `n` is an integer, and if `n` is less than or equal to `0`, it returns an empty list.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): I created a Python function that inserts a line of text into a file after each line containing a specified string.

* **14. Log parsing**
  * [101-stats.py](./101-stats.py): This Python script reads lines from standard input. After every 10 lines or upon receiving a keyboard interruption (`CTRL + C`), it computes various metrics, including the total file size up to that point and the status code of each read line, printed in ascending order. The input format for this script is `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`.
