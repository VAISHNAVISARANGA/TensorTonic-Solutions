import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Check if input is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        return None

    # Check if it's a list of lists
    if not all(isinstance(row, list) for row in matrix):
        return None

    n = len(matrix)

    # Check square matrix
    if not all(len(row) == n for row in matrix):
        return None

    return np.linalg.eigvals(matrix)