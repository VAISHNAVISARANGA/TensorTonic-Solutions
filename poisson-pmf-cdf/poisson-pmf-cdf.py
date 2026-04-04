import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    fact=np.prod(np.arange(1,k+1))
    pmf=(np.exp(-lam)*lam**k)/fact
    cdf=0
    for i in range(k+1):
        if i>0:
            fact=np.prod(np.arange(1, i+1))
        else:
            fact=1
        cdf+=(np.exp(-lam)*lam**i)/fact
        

    return pmf, cdf