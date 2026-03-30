import numpy as np

def geometric_pmf_mean(k, p):
    pmf=[]
    k= np.array(k)
    pmf=(1-p)**(k-1)*p
    mu=1/p
    return np.array(pmf), mu