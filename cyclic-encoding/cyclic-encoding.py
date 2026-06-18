import numpy as np
import math
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    values=np.array(values)
    if period==0:
        return None
    theta=(2*math.pi*values)/period
    encoded=np.column_stack((np.sin(theta), np.cos(theta)))
    return encoded.tolist()