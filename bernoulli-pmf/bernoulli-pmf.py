import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x=np.array(x)
    if not np.all((x==0) | (x==1)):
        return None
    pmf= p**x*(1-p)**(1-x)    
    mu=p
    var=p*(1-p)
    

    return (pmf,mu, var)
    pass