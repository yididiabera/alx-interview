#!/usr/bin/python3
"""
Module for island_perimeter
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    """
    n = len(grid)
    m = len(grid[0])
    peri = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if i == 0:
                    peri += 1
                elif grid[i-1][j] == 0:
                    peri += 1
                if i == n-1:
                    peri += 1
                elif grid[i+1][j] == 0:
                    peri += 1
                if j == 0:
                    peri += 1
                elif grid[i][j-1] == 0:
                    peri += 1
                if j == m-1:
                    peri += 1
                elif grid[i][j+1] == 0:
                    peri += 1
    return peri
