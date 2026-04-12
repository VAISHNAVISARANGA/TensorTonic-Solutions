import numpy as np

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points=np.asarray(points)
    centroids=np.asarray(centroids)

    assignments=[]

    for p in points:
        distances=np.sum((p-centroids)**2, axis=1)
        best_idx=np.argmin(distances)
        assignments.append(best_idx)

    return np.array(assignments).tolist()