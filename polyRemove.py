import numpy as np
import math
class PolyRemove:
    def __init__(self, x, y, order=1):
        z = np.polyfit(x, y, order)
        p = np.poly1d(z)
        self.polyArray = self.arrayFromPoly(p, len(x), x[0])
        self.data = y-self.polyArray

    def arrayFromPoly(self, poly, size, start=0):
        array = np.array([])
        for i in range(size):
            array = np.append(array, [poly(i+math.floor(start))])
        print(array)
        return array