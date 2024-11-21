#!/usr/bin/python3
"""A module for rotating a 2D matrix 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Rotates a given square 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A 2D list representing the square matrix to be rotated.
    """
    n = len(matrix)  # Get the size of the matrix (n x n)

    # Loop through each layer of the matrix
    for layer in range(n // 2):
        # Loop through elements in the current layer
        for element in range(layer, n - layer - 1):
            # Store the top element temporarily
            top_element = matrix[layer][element]

            # Move the left element to the top
            matrix[layer][element] = matrix[n - 1 - element][layer]

            # Move the bottom element to the left
            matrix[n - 1 - element][layer] = matrix[n - 1 - layer][n - 1 - element]

            # Move the right element to the bottom
            matrix[n - 1 - layer][n - 1 - element] = matrix[element][n - 1 - layer]

            # Move the top element (stored earlier) to the right
            matrix[element][n - 1 - layer] = top_element

