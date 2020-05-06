from scipy.spatial import cKDTree
import numpy as np

def process(path, distance_bound = 3):
    points = np.array(path)
    for item in points:
        distance = cKDTree(points)
        d,_ = distance.query(item, 2, distance_upper_bound=distance_bound)
        if d[1]:
            points = np.delete(points,[_[1]],axis = 0)
