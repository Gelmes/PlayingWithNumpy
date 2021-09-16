import numpy as np
import math
class ExpRemove:
    def __init__(self, x, y, order=1):
        print(x)
        z = np.polyfit(x-x[0], np.log(y), order)
        p = np.poly1d(z)
        self.array = np.exp( z[0] ) * np.exp( z[1] * x-x[0] )
        print(self.array)
        # self.array = self.arrayFromPoly(p, len(x), x[0])
        # self.data = y-self.polyArray

    def arrayFromPoly(self, poly, size, start=0):
        array = np.array([])
        for i in range(size):
            array = np.append(array, [poly(i+math.floor(start))])
        return array