import numpy as np
def gini(y):
    y=np.array(y)
    labels, counts=np.unique(y, return_counts=True)
    p=counts/len(y)
    return 1-np.sum(p**2)
def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    # Write code here
    best_feature= None
    best_threshold= None
    best_gain=-1
    X=np.array(X)
    y= np.array(y)
    n= X.shape[1]
    gini_parent= gini(y)
    for feature in range(n):
        values=X[:, feature]
        counts=np.sort(np.unique(values))
        thresholds=[]
        for i in range(len(counts)-1):
            t=(counts[i]+counts[i+1])/2
            thresholds.append(t)
        for t in thresholds:
            left= values<=t
            right= values>t
            y_left=y[left]
            y_right= y[right]
            gini_left=gini(y_left)
            gini_right= gini(y_right)
            gini_child= len(y_left)/len(values)*gini_left+ len(y_right)/len(values)*gini_right
            gain= gini_parent- gini_child
            if gain>best_gain:
                best_gain= gain
                best_threshold= t
                best_feature= feature
    return best_feature, best_threshold
                
            
            