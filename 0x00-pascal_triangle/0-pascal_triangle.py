#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Creating a function def pascal_triangle(n): it returns a list of lists of integers that represent the Pascal’s triangle of n
    """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            result.append(level)
    return result
