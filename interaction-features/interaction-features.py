import numpy as np

def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    output=[]
    X=np.array(X)
    samples, features= X.shape
    for i in range(features):
        for j in range(i+1, features):
            output.append(X[:,i]*X[:,j])
    if len(output)==0:
        return X.tolist()
    output=np.array(output).T
    interactions=np.hstack((X, output))
    return interactions.tolist()