import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    X_train=np.array(X_train)
    X_test=np.array(X_test)
    n=X_train.shape[0]
    if X_train.ndim==1:
        X_train=X_train.reshape(-1, 1)
    if X_test.ndim==1:
        X_test=X_test.reshape(-1, 1)
    dist=np.sqrt(np.sum((X_train[np.newaxis,:,:]-X_test[:,np.newaxis,:])**2, axis=2))
    idx=np.argsort(dist, axis=1)

    if(k<=n):
        return idx[:, :k]
    output= np.full((X_test.shape[0], k), -1)
    output[:,:n]=idx
    

    return output
    

        