import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x= np.array(x)
    n= len(x)
    x_bmean=[]
    for i in range(n_bootstrap):
        x_b=rng.choice(x, size=n, replace=True)
        val=np.mean(x_b)
        x_bmean.append(val)
    x_bmean=np.array(x_bmean)
    alpha=(1-ci)/2
    lower= np.quantile(x_bmean,alpha)
    upper=np.quantile(x_bmean, 1-alpha)
    return x_bmean, lower, upper
  
