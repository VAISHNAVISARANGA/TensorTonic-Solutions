def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)
    x1=np.dot(X.T , X)
    I=np.eye(x1.shape[0])
    x2=lam*I
    x3=np.dot(X.T , y)
    one= np.linalg.inv(x1+x2) 
    w= np.dot(one, x3)
    return w