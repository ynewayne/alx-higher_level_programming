This readme contains the directions to construct the 0x08-python-more_classes project in ALX higher level programming.

The file names and the function of each script are detailed below.

0-rectangle.py - Write an empty class Rectangle that defines a rectangle

1-rectangle.py - Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError exception with the message height must be >= 0
Instantiation with optional width and height: def __init__(self, width=0, height=0):
You are not allowed to import any module

2-rectangle.py - Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError exception with the message height must be >= 0
Instantiation with optional width and height: def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0
You are not allowed to import any module

3-rectangle.py - Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError exception with the message height must be >= 0
Instantiation with optional width and height: def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #: (see example below)
if width or height is equal to 0, return an empty string
You are not allowed to import any module

4-rectangle.py - This Python class defines a rectangle and extends the functionality of 3-rectangle.py by introducing a special method called __repr__ that returns a string representation of the rectangle.

5. Detecting Instance Deletion

5-rectangle.py: In this Python class, a rectangle is defined, building upon the features of 4-rectangle.py. It includes a special method named __del__, which is responsible for printing the message "Bye rectangle..." when a Rectangle instance is deleted.

6. Counting Instances

6-rectangle.py: This Python class defines a rectangle and extends the functionalities of 5-rectangle.py. It introduces a public class attribute called number_of_instances, initially set to 0, which is incremented each time a new instance is created and decremented when an instance is deleted.

7. Changing Representation

7-rectangle.py: This Python class defines a rectangle, building upon the features of 6-rectangle.py. It introduces a public class attribute called class_symbol, initially set to #, but it can be customized to any desired symbol. This symbol is used in the string representation of the rectangle.
8. Comparing Rectangles

8-rectangle.py: This Python class defines a rectangle and extends the functionality of 7-rectangle.py. It includes a static method named bigger_or_equal(rect_1, rect_2), which returns the rectangle with the greater area. If both areas are equal, it returns rect_1. Additionally, if either rect_1 or rect_2 is not an instance of the Rectangle class, a TypeError is raised with a specific error message.
9. A Square is a Special Rectangle

9-rectangle.py: This Python class defines a rectangle and extends the features of 8-rectangle.py. It introduces a class method called square(cls, size=0), which creates a new Rectangle instance with both width and height set to the same value, specified by the size parameter.
10. Solving the N Queens Puzzle

alt text

101-nqueens.py: This Python program is designed to solve the N queens puzzle. It takes the value of N as a command-line argument.
To use the program, run it as follows: ./101-nqueens.py N.
It calculates and lists all possible solutions for placing N non-attacking queens on an NxN chessboard.
The program requires exactly two arguments to be provided. Otherwise, it will display the message "Usage: nqueens N" and exit with a status code of 1.
If the provided N is not an integer, the program will print "N must be a number" and exit with a status code of 1.
If the provided N is less than 4, the program will print "N must be at least 4" and exit with a status code of 1.
The solutions are presented one per line in the format [[r, c], [r, c], [r, c], [r, c]], where r and c represent the row and column, respectively, where a queen must be placed.



 
