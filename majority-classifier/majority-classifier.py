import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    X_test=np.array(X_test)
    y_train=np.array(y_train)
    labels, counts=np.unique(y_train, return_counts=True)
    idx=labels[np.argmax(counts)]
    output=np.full(len(X_test), idx)
    return output
    pass