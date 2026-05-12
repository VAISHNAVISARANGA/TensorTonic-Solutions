import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    output=[]
    predictions=np.array(predictions)
    for i in range(predictions.shape[1]):
        column=predictions[:,i]
        labels, counts=np.unique(column, return_counts=True)
        majority_label=labels[np.argmax(counts)]
        output.append(majority_label)
    return output