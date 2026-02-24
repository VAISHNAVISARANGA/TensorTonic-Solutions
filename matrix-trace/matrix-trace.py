import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    total=0
    N=len(A);
    for i in range(N):
        for j in range(N):
            if i==j: 
                total+=A[i][j]
    return total
    pass
