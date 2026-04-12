import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left=np.asarray(y_left)
    y_right= np.asarray(y_right)

    value_left, count_left= np.unique(y_left, return_counts=True)
    value_right, count_right= np.unique(y_right, return_counts=True)
    p_left=count_left/len(y_left)
    p_left=p_left[p_left>0]
    p_right= count_right/len(y_right)
    p_right=p_right[p_right>0]

    gini_left=1-np.sum(p_left**2)
    gini_right=1-np.sum(p_right**2)

    N_l= len(y_left)
    N_r=len(y_right)
    N=N_l+N_r
    if (N>0):
        gini=(N_l/N)*gini_left + (N_r/N)*gini_right
    else:
        gini=0
    return float(gini)
