import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    TP = np.sum(y_true == y_pred)
    FP = len(y_pred) - TP
    FN = len(y_true) - TP

    denom = 2 * TP + FP + FN
    return 2 * TP / denom if denom != 0 else 0.0
    pass