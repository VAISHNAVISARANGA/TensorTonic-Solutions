import numpy as np
from collections import Counter

def mean_median_mode(x):
    x=np.array(x)
    mean= np.mean(x)
    median= np.median(x)
    freq= Counter(x)
    mode= max(freq, key= freq.get)
    return mean, median, mode

    