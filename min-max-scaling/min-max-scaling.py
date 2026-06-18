import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data=np.array(data)
    min=np.min(data, axis=0)
    max=np.max(data,axis=0)
    range=max-min;
    if np.any(range==0):
        return np.zeros((data.shape)).tolist()
    return ((data - min) / range).tolist()