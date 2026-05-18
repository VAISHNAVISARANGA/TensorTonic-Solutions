import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    predictions=np.array(predictions)
    K=len(predictions)
    q=np.full(K, epsilon/K)
    q[target]= (1-epsilon)+(epsilon/K)
    loss=- np.sum(q *np.log(predictions))
    return loss
    