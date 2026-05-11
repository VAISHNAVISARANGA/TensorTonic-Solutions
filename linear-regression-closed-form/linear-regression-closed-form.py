import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)
    x1=np.dot(X.T, X)
    x1=np.linalg.inv(x1)
    x2=X.T @y
    w=x1@x2
    return w
    pass