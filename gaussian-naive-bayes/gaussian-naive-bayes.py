import numpy as np
def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    epsilon=1e-9;
    X_train=np.array(X_train)
    X_test=np.array(X_test)
    y_train=np.array(y_train)
    classes=np.unique(y_train)
    
    means={}
    variance={}
    priors={}
    for c in classes:
        X= X_train[y_train==c]
        priors[c]=len(X)/len(X_train)
        if X.ndim==1:
            X=X.reshape(-1, 1)
        means[c]=np.mean(X, axis=0)
        variance[c]=np.var(X, axis=0)+ epsilon
    predictions=[]
    for x in X_test:
        posteriors=[]

        for c in classes:
            mean=means[c]
            var=variance[c]
            log_prior=np.log(priors[c])
            likelihood=np.sum(-0.5*np.log(2*3.14*var)- ((x-mean)**2)/(2*var))
            log_posterior=log_prior+likelihood

            posteriors.append(log_posterior)
        predictions.append(classes[np.argmax(posteriors)])
    return predictions
        
