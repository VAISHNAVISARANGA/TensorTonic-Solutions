import numpy as np
def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # Write code here
    grad=np.array(grad)
    s_list= np.array(s_list)
    y_list= np.array(y_list)
    m= len(s_list)
    q=grad.copy()
    alpha=np.zeros(m)
    rho=[1/_dot(y_list[i], s_list[i]) for i in range(m)]
    for i in range(m-1, -1, -1):
        alpha[i]= rho[i]*_dot(s_list[i], q)
        q= q-alpha[i]*y_list[i]
    gamma= _dot(s_list[-1], y_list[-1])/_dot(y_list[-1], y_list[-1]) if m>0 else 1
    r=gamma*q
    for i in range(m):
        beta=rho[i]*_dot(y_list[i], r)
        r=r+s_list[i]*(alpha[i]-beta)
   
    return -r
