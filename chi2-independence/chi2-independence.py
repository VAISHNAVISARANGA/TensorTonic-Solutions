import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C=np.array(C)
    R1= np.sum(C, axis=1)
    C1= np.sum(C, axis=0)
    total=np.sum(C)
    expected=np.outer(R1, C1)/total
    chi2= np.sum(((C-expected)**2)/expected)
    return chi2, expected