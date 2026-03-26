import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    if len(a)!=len(b): 
        return None
    n=np.linalg.norm(a)
    m= np.linalg.norm(b)
    if n==0 or m==0:
        return 0
    cosine= np.dot(a, b)/(n*m) 
    return float(cosine)
    pass