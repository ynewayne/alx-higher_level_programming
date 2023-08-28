#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integer elements from a list.

    Args:
        my_list (list): The list containing elements to print.
        x (int): The number of elements from my_list to print.

    Returns:
        The count of printed integer elements.
    """
    count = 0  # Initialize the count of printed integers
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")  # Print the integer element
            count += 1  # Increment the count of printed integers
        except (ValueError, TypeError):
            continue  # Ignore non-integer elements
    print("")  # Print a newline after printing the elements
    return count  # Return the count of printed integers
