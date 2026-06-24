import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)
    indices=np.arange(len(X))
    if rng==None:
        np.random.shuffle(indices)
    else:
        rng.shuffle(indices)
    if drop_last:
        end=(len(X)//batch_size)*batch_size
    else:
        end=len(X)
    for i in range(0, end, batch_size):
        stop=i+batch_size

        if stop>len(X) and drop_last:
            break
        batch_idx=indices[i:stop]
        yield X[batch_idx], y[batch_idx]
   
    pass