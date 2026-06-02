import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    y_mean=np.mean(y_true)
    if np.all(y_true[0]==y_true):
        if np.all(y_true==y_pred):
            return 1.0
        else:
            return 0.0
    r2=1-((np.sum((y_true-y_pred)**2))/(np.sum((y_true-y_mean)**2)))
    return r2
    pass