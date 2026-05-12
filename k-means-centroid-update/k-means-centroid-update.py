import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    assignments=np.array(assignments)
    points=np.array(points)
    centroids=[]
    for i in range(k):
        cluster_points= points[assignments==i]
        if(len(cluster_points)>0):
            centroid=np.mean(cluster_points, axis=0)
        else:
            if points.ndim==1:
                centroid=0
            else:
                centroid=np.zeros(points.shape[1])
        centroids.append(centroid.tolist())
        
    return centroids
    