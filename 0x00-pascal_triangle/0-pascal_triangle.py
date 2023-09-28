#!/usr/bin/python3
"""
This script defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows (> 0).

    Returns:
        list of lists: Pascal's Triangle as a list of lists.
    """
    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            # Calculate the values for the current row based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)

    return triangle
