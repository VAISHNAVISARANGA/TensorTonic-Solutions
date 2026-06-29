import numpy as np
from sklearn.impute import SimpleImputer
def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X=np.array(X)
    imputer = SimpleImputer(strategy=strategy, keep_empty_features=True)
    if X.ndim==1:
        X_imputed=imputer.fit_transform(X.reshape(-1, 1)).ravel()
    else:
        X_imputed = imputer.fit_transform(X)
    X_imputed=np.nan_to_num(X_imputed, nan=0)
    return X_imputed
                
                
    pass