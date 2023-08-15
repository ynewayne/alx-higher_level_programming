This project provided an opportunity to explore sequence data types within Python, specifically focusing on lists and tuples.

Testing :heavy_check_mark:
tests: This directory contains test files, provided by ALX School.
Function Declarations :floppy_disk:
Outlined below are the function prototypes implemented within this project:

File	Function Prototype
0-print_list_integer.py	def print_list_integer(my_list=[]):
1-element_at.py	def element_at(my_list, idx):
2-replace_in_list.py	def replace_in_list(my_list, idx, element):
3-print_reversed_list_integer.py	def print_reversed_list_integer(my_list=[]):
4-new_in_list.py	def new_in_list(my_list, idx, element):
5-no_c.py	def no_c(my_string):
6-print_matrix_integer.py	def print_matrix_integer(matrix=[[]]):
7-add_tuple.py	def add_tuple(tuple_a=(), tuple_b=()):
8-multiple_returns.py	def multiple_returns(sentence):
9-max_integer.py	def max_integer(my_list=[]):
10-divisible_by_2.py	def divisible_by_2(my_list=[]):
11-delete_at.py	def delete_at(my_list=[], idx=0):
100-print_python_list_info.c	void print_python_list_info(PyObject *p);
Tasks :page_with_curl:
Each task within this project has been summarized as follows:

0. Printing List Elements

0-print_list_integer.py: A Python function to print all integers within a list, one per line.
Achieved without importing modules or converting integers to strings.
1. Safe List Element Access

1-element_at.py: A Python function to retrieve an element from a list.
Returns None for negative or out-of-range indices.
Implemented without importing modules or using try/except.
2. Replacing List Elements

2-replace_in_list.py: A Python function to replace an element within a list at a specific position.
Returns the original list for negative or out-of-range indices.
Implemented without importing modules or using try/except.
3. Reversed List Printing

3-print_reversed_list_integer.py: A Python function to print integers from a list in reverse order, one per line.
Achieved without importing modules or converting integers to strings.
4. Replacement in a Copied List

4-new_in_list.py: A Python function to replace an element within a list at a specific position without modifying the original list.
Returns the original list for negative or out-of-range indices.
Implemented without importing modules or using try/except.
5. Character Removal from Strings

5-no_c.py: A Python function to remove all occurrences of characters c and C from a string.
Achieved without importing modules or using str.replace().
6. Matrices and Nested Lists

6-print_matrix_integer.py: A Python function to print a matrix of integers, one row per line.
Achieved without converting integers to strings.
7. Tuple Addition

7-add_tuple.py: A Python function to add two tuples.
Returns a tuple containing the element-wise addition of corresponding tuple elements.
Handles tuples smaller or larger than 2 elements.
Implemented without importing modules.
8. String Length and First Character

8-multiple_returns.py: A Python function to return a tuple containing the length of a string and its first character.
Handles empty strings.
Implemented without importing modules.
9. Finding the Maximum Integer

9-max_integer.py: A Python function to find the largest integer within a list.
Returns None for empty lists.
Implemented without importing modules or using the built-in max().
10. Identifying Multiples of 2

10-divisible_by_2.py: A Python function to identify multiples of 2 in a list and return a corresponding boolean list.
Implemented without importing modules.
11. Deletion at Specific Position

11-delete_at.py: A Python function to delete an item at a specific position within a list.
Returns the original list for negative or out-of-range indices.
Implemented without importing modules or using pop().
12. Variable Value Swapping

12-switch.py: A Python program to swap the values of variables a and b.
13. Linked List Palindrome

13-is_palindrome.c: A C function to determine if a singly-linked list is a palindrome.
Returns 1 for palindrome, 0 otherwise.
Considers empty lists as palindromes.
Helper files: linked_lists.c and lists.h.
14. CPython #0: Python Lists

100-print_python_list_info.c: A C function to display basic information about Python lists.
