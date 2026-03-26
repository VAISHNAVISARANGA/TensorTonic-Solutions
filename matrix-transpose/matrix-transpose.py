import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n= len(A)
    m= len(A[0])
    T = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            T[j][i]= A[i][j]
    return np.array(T)
    pass
