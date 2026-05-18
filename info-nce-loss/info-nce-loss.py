import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1=np.array(Z1)
    Z2=np.array(Z2)
    S=np.dot(Z1, Z2.T)/ temperature
    S=S-np.max(S, axis=1, keepdims=True)
    loss=-np.mean(np.log(np.exp(np.diag(S))/ np.sum(np.exp(S), axis=1)))
    return loss
    pass