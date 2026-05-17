import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1=np.array(x1)
    x2=np.array(x2)
    cos=(np.dot(x1, x2))/(np.linalg.norm(x1)*np.linalg.norm(x2))
    if label==1:
        loss= 1-cos
    else:
        loss=np.maximum(0, cos-margin)
    return float(loss)