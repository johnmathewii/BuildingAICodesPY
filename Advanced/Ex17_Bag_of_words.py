import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    diff = 0
    for ro1,ro2 in zip(row1,row2):
        diff += abs(ro1 - ro2)
    return diff    

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float64)
    for i, datai in enumerate(data):
        for j, dataj in enumerate(data):
            if (i == j):
                dist[i][j] = np.inf
            else:
                dist[i][j] = distance(datai, dataj)
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
