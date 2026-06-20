import numpy as np
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    
    original=np.array(values)
    values=np.sort(np.array(values))
    if len(values)==1: 
        return [0]
    median=np.median(values)
    n=len(values)
    if n%2==0:
        lower=values[:n//2]
        upper=values[n//2:]
    else:
        lower=values[:n//2]
        upper=values[n//2+1:]
    Q1=np.median(lower)
    Q3=np.median(upper)

    IQR=Q3-Q1
    if IQR==0:
        output= original-median
    else:
        output=(original-median)/IQR
    return output