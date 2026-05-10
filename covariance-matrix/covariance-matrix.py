import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    
    X=np.array(X)
    if X.ndim==1:
        return None
    mu=np.mean(X, axis=0)
    X_centered=X-mu
    N=X.shape[0]
    if N==1:
        return None
    else:
        cov=1/(N-1)*np.dot(X_centered.T,X_centered)
    return cov
    pass