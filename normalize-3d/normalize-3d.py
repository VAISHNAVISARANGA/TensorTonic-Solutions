import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v=np.asarray(v)
    if v.ndim==1:
        norm=np.sqrt(np.sum(v**2))
        return v/norm if norm>1e-10 else v
    else:
      
        val=np.sum(v**2, axis=1, keepdims=True)
        norm= np.sqrt(val)
        norm[norm<1e-10]=1
        return v/norm 
    