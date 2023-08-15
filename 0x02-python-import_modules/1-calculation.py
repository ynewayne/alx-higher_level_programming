#!/usr/bin/python3

if __name__ == "__main__":
    """Calculate and display the sum, difference, product, and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    first_number = 10
    second_number = 5

    print("{} + {} = {}".format(first_number, second_number, add(first_number, second_number)))
    print("{} - {} = {}".format(first_number, second_number, sub(first_number, second_number)))
    print("{} * {} = {}".format(first_number, second_number, mul(first_number, second_number)))
    print("{} / {} = {}".format(first_number, second_number, div(first_number, second_number)))
