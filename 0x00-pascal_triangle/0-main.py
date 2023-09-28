#!/usr/bin/python3
"""
This script is the main module for generating and printing Pascal's Triangle.
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the Pascal's Triangle.
    """
    # Iterate through each row in the triangle and print it
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Generate and print Pascal's Triangle with 5 rows
    print_triangle(pascal_triangle(5))
