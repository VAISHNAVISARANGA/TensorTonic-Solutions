import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix=np.array(matrix)
    if matrix.ndim!=2:
        return None
    if axis==0:
        if norm_type=='l2':
            total=np.sqrt(np.sum(matrix**2, axis=0))
            if total==0:
                total=1
            matrix=matrix/total
        elif norm_type=='l1':
            total=np.sum(matrix, axis=0)
            total[total==0]=1
            matrix=matrix/total
        elif norm_type=='max':
            total=np.max(matrix, axis=0)
            total[total==0]=1
            matrix=matrix/total
        else:
            return None
        
    elif axis==1:
        if norm_type=='l2':
            total=np.sqrt(np.sum(matrix**2, axis=1))
            total[total==0]=1
            matrix=matrix/total.reshape(-1, 1)
        elif norm_type=='l1':
            total=np.sum(matrix, axis=1)
            total[total==0]=1
            matrix=matrix/total.reshape(-1,1)
        elif norm_type=='max':
            total=np.max(matrix, axis=1)
            total[total==0]=1
            matrix=matrix/total.reshape(-1,1)
        else:
            return None
    elif axis==None:
        if norm_type=='l2':
            total=np.sqrt(np.sum(matrix**2))
            total[total==0]==1
            matrix=matrix/total
        elif norm_type=='l1':
            total=np.sum(matrix, axis=0)
            total[total==0]=1
            matrix=matrix/total
        elif norm_type=='max':
            total=np.max(matrix)
            total[total==0]=1
            matrix=matrix/total
        else:
            return None
    else:
        return None

    return matrix
    pass