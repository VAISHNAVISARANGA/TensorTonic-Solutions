import numpy as np
import scipy
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    cdf=0;
    pmf= scipy.special.comb(n, k)*p**k*(1-p)**(n-k)
    for i in range(k+1):
        cdf+=scipy.special.comb(n, i)*p**i*(1-p)**(n-i)
        
    return float(pmf), float(cdf)