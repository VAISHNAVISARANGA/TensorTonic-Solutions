import numpy as np
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    values=np.array(values)
    output=[]
    for i in range(degree+1):
        output.append(values**i)
    return np.array(output).T.tolist()