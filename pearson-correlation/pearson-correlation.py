import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X=np.array(X)
    mu=np.mean(X, axis=0)
    X_centered=X-mu
    n=X.shape[0]
    cov=(X_centered.T@X_centered)/(n-1)
    std=np.sqrt(np.diag(cov))
    corr=cov/np.outer(std, std)
    return corr
    pass