import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x=np.array(x)
    mu=np.mean(x)
    n=len(x)
    
    std=np.sqrt((np.sum((x-mu)**2))/(n-1))
    d=std/np.sqrt(n)
    t= (mu-mu0)/d
    return t