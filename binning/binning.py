import numpy as np

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values=np.array(values)
    min_val=np.min(values)
    max_val=np.max(values)
    if min_val==max_val:
        return [0]*len(values)
    w=(np.max(values)-np.min(values))/num_bins
    bin=np.minimum(((values-np.min(values))/w).astype(int), num_bins-1)
    return bin.tolist()