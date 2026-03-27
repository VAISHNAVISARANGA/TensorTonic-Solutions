import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    n=len(A)
    m=len(A[0])
    if(n!=m):
        return None
    elif(np.linalg.det(A)==0):
        return None
    else:
       return np.linalg.inv(A)
    

    
    pass
