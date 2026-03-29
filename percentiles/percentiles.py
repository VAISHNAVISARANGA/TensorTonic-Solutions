import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    n= len(x)
    x=np.sort(x)
    ans=[]
    for p in q:
        L= (p/100)*(n-1)
        if L<0:
            ans.append(x[0])
        elif L>n:
            ans.append(x[n-1])
       
    
        lower= int(np.floor(L))
        upper= lower+1
        if lower== n-1:
            ans.append(x[lower])

        elif lower==upper:
            ans.append(x[lower])
        else:
            weight= abs(L- lower)
            val= x[lower]+weight*(x[upper]- x[lower])
            ans.append(val)
    ans= np.array(ans)        
    return ans