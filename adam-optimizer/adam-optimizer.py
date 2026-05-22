import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param=np.array(param)
    grad=np.array(grad)
    v=np.array(v)
    m=np.array(m)
    
    m=beta1*m +(1-beta1)*grad
    v=beta2*v +(1-beta2)*(grad**2)
    m_hat=m/(1-beta1**t)
    v_hat= v/(1-beta2**t)
    param= param- ((m_hat)/(np.sqrt(v_hat)+eps))*lr
    return param, m, v
    pass