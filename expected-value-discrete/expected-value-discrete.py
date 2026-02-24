import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    sum=0
    x= np.array(x)
    p=np.array(p)
    if len(x)!=len(p):
        raise ValueError("x and p ust have equal lengths")
    elif np.sum(p)!=1:
        raise ValueError(" ")
    sum=np.sum(x*p)
    return sum
    pass
