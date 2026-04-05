import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    points= np.asarray(points)
    if points.ndim == 1:
        x, y, z = points  # preserve originals
        
        x_new = x*np.cos(theta) - y*np.sin(theta)
        y_new = x*np.sin(theta) + y*np.cos(theta)
        
        return np.array([x_new, y_new, z])
    
    else:
        x =points[:,0]
        y =points[:,1]
        z= points[:, 2]
        
        x_new =x*np.cos(theta) - y*np.sin(theta)
        y_new = x*np.sin(theta) + y*np.cos(theta)
        return np.stack([x_new,y_new, z], axis=1)
    