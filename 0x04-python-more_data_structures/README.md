In this programming exercise, I gained an understanding of sets and dictionaries in Python and practiced their usage alongside the lambda, map, filter, and reduce methods.

Test Files :heavy_check_mark:
tests: This directory contains test files provided by Holberton School to validate the code.
Function Prototypes :floppy_disk:
Below are the prototypes for the functions developed in this exercise:

File	Prototype
0-square_matrix_simple.py	def square_matrix_simple(matrix=[]):
1-search_replace.py	def search_replace(my_list, search, replace):
2-uniq_add.py	def uniq_add(my_list=[]):
3-common_elements.py	def common_elements(set_1, set_2):
4-only_diff_elements.py	def only_diff_elements(set_1, set_2):
5-number_keys.py	def number_keys(a_dictionary):
6-print_sorted_dictionary.py	def print_sorted_dictionary(a_dictionary):
7-update_dictionary.py	def update_dictionary(a_dictionary, key, value):
8-simple_delete.py	def simple_delete(a_dictionary, key=""):
9-multiply_by_2.py	def multiply_by_2(a_dictionary):
10-best_score.py	def best_score(a_dictionary):
11-mutiply_list_map.py	def mutiply_list_map(my_list=[], number=0):
12-roman_to_int.py	def roman_to_int(roman_string):
100-weight_average.py	def weight_average(my_list=[]):
101-square_matrix_map.py	def square_matrix_map(matrix=[]):
102-complex_delete.py	def complex_delete(a_dictionary, value):
103-python.c	<ul><li>void print_python_list(PyObject *p);</li><li>void print_python_bytes(PyObject *p);</li></ul>
Tasks :page_with_curl:
0. Squared simple

0-square_matrix_simple.py: This Python function computes the square value of all integers within a matrix.
The matrix parameter is a two-dimensional array.
The function returns a matrix of the same size as matrix, where each value is the square of the corresponding input value.
The original matrix remains unchanged.
No external modules are imported.
1. Search and replace

1-search_replace.py: This Python function replaces all occurrences of a given element with another in a new list.
The my_list parameter represents the initial list.
The search parameter is the element to be replaced in the list.
The replace parameter is the new element to replace with.
No external modules are imported.
2. Unique addition

2-uniq_add.py: This Python function adds all unique integers in a list, considering each integer only once.
No external modules are imported.
3. Present in both

3-common_elements.py: This Python function returns a set of common elements between two sets.
No external modules are imported.
4. Only differents

4-only_diff_elements.py: This Python function returns a set of elements that are present in only one of the input sets.
No external modules are imported.
5. Number of keys

5-number_keys.py: This Python function returns the number of keys in a dictionary.
No external modules are imported.
6. Print sorted dictionary

6-print_sorted_dictionary.py: This Python function prints a dictionary with keys sorted in alphabetical order.
The function assumes all keys are strings.
Only the first level of keys is sorted.
The dictionary values can have any type.
No external modules are imported.
7. Update dictionary

7-update_dictionary.py: This Python function replaces or adds key/value pairs in a dictionary.
The key parameter is always a string.
The value parameter can be of any type.
If the key already exists in the dictionary, its value is replaced.
If the key does not exist, a new key-value pair is created.
No external modules are imported.
8. Simple delete by key

8-simple_delete.py: This Python function deletes a key from a dictionary.
The key parameter is always a string.
If the key does not exist, the dictionary remains unchanged.
No external modules are imported.
9. Multiply by 2

9-multiply_by_2.py: This Python function returns a new dictionary with all values multiplied by 2.
The function assumes all values in the dictionary are integers.
No external modules are imported.
10. Best score

10-best_score.py: This Python function returns the key with the highest integer value from a dictionary.
The function assumes all values in the dictionary are integers.
The function assumes all students have distinct scores.
If no valid score is found, the function returns None.
No external modules are imported.
11. Multiply by using map

11-mutiply_list_map.py: This Python function returns a list with all values multiplied by a given number using the map function.
The resulting list has the same length as the input list, and each value is multiplied by the specified number.
The original list remains unchanged.
Loops are avoided, and no external modules are imported.
12. Roman to Integer

12-roman_to_int.py: This Python function converts a Roman numeral to an integer.
The function is designed for Roman numerals between 1 and 3999.
If the roman_string parameter is not a string or is None, the function returns 0.
13. Weighted average!

100-weight_average.py: This Python function calculates the weighted average of all integers in a list of tuples.
The tuple format is (<score>, <weight>).
If the list is empty, the function returns 0.
No external modules are imported.
14. Squared by using map

101-square_matrix_map.py: This Python function computes the square value of all integers in a matrix using the map function.
The matrix parameter is a two-dimensional array.
The function returns a new matrix of the same size as the input matrix, with each value squared.
The original matrix remains unchanged.
Loops are avoided, and no external modules are imported.
15. Delete by value

102-complex_delete.py: This Python function deletes keys with a specific value from a dictionary.
If the value does not exist, the dictionary remains unchanged.
All keys with the specified value are removed.
No external modules are imported.
16. CPython #1: PyBytesObject

103-python.c: This set of C functions prints basic information about Python lists and Python bytes objects.
