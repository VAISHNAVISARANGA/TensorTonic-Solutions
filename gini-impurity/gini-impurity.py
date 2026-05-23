import numpy as np
def _gini(p):
    label, count= np.unique(p, return_counts=True)
    p=count/np.sum(count)
    return 1-np.sum(p**2)
def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left= np.array(y_left)
    y_right=np.array(y_right)
    N_L=len(y_left)
    N_R=len(y_right)
    N=N_L+N_R
    if(N!=0):
        gini_split= (N_L/N)*(_gini(y_left))+(N_R/N)*(_gini(y_right))
    else:
        gini_split=0
    return float(gini_split)
    
    pass