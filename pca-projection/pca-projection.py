import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X=np.array(X)
    mu= np.mean(X, axis=0)
    X_centered=X-mu
    n=X.shape[0]
    C=1/(n-1)* np.dot(X_centered.T , X_centered)
    eigenvalues, eigenvectors=np.linalg.eigh(C)
    idx=np.argsort(eigenvalues)[::-1]
    eigenvalues= eigenvalues[idx]
    eigenvectors= eigenvectors[:,idx]
    W=eigenvectors[:,:k]
    X_proj= X_centered @ W
    return X_proj
    