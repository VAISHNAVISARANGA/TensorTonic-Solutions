import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v= np.asarray(v)
    w= np.asarray(w)
    v_norm=np.sqrt(np.sum(v**2))
    w_norm=np.sqrt(np.sum(w**2))
    cos_theta= np.dot(v, w)/(v_norm*w_norm)
    theta=np.arccos(cos_theta)
    return theta
   