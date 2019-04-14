import numpy as np

class Direction(np.array) :
    def __init__(self, coords):
        if np.linalg.norm(np.array(coords)) != 1 and (coords[0] != 0 or coords[1] != 0) :
            coords == (0, 1)
        self = np.array(coords)


