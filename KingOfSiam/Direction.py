import numpy as np


class Direction(np.ndarray):
    def __new__(cls, data):
        if np.linalg.norm(np.array(data)) == 1 and (data[0] != 0 or data[1] != 0):
            direction = np.asarray(data).view(cls)
            return direction
        elif np.linalg.norm(np.array(data)) != 1:
            raise ValueError("The direction is not an unitary vector !")
        elif data[0] != 0 or data[1] != 0:
            raise ValueError("The direction must have a null coordinate !")

    def __init__(self, data):
        self.angle = np.arccos(np.array([1, 0]) @ self)

    def bearing(self, other):
        return other @ self

    def scalar(self, others):
        result = 0
        is_negative = False
        for other in others:
            result += self.bearing(other)
            if result < 0:
                is_negative = True
                break
        return int(result), is_negative

if __name__ == '__main__':
    a = Direction([1, 0])
    print(a.scalar([np.array([1, 0]), np.array([-1, 0]), np.array([-1, 0])]))