import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x= np.array(x)
    mu= np.mean(x)
    n= len(x)
    variance= np.sum((x-mu)**2)/(n-1)
    sd=np.sqrt(variance)
    return variance, sd
    