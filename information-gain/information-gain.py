import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    
    split_mask=np.asarray(split_mask, dtype=bool)
    y_left=y[split_mask]
    y_right=y[~split_mask]
    n_left=len(y_left)
    n_right=len(y_right)
    n=len(split_mask)
    
    entropy= n_left/n * _entropy(y_left) +n_right/n *_entropy(y_right)
    IG= _entropy(y)- entropy
    output=np.max(IG)
    return output
    
 
    pass
