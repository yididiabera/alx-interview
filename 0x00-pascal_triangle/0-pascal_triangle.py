#!/usr/bin/python3
'''Solution of Pascal's Triangle'''


def pascal_triangle(n):
    '''Pascal's Triangle Function'''
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(n - 1):
        temp = [0] + pascal[-1] + [0]
        pascal_row = []
        for j in range(len(pascal[-1]) + 1):
            pascal_row.append(temp[j] + temp[j+1])
        pascal.append(pascal_row)
    return pascal
