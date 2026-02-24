import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x=np.array(x)
    y=np.array(y)
    if len(x)!=len(y):
        raise ValueError("")
    total=0
    total=np.sum((x-y)**2)
    return float(np.sqrt(total))
    pass