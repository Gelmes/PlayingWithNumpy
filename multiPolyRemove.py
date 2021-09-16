
import pandas as pd
from polyRemove import PolyRemove

class MultiPolyRemove:
    def __init__(self, x, data, samples=3, order=2):
        
        # if (type(data) == pd.core.frame.DataFrame):
        #     self.dataFrame = data
        # else:
        #     self.dataFrame = pd.DataFrame(data)
        self.data = data
        for i in range(samples):
            self.data =  PolyRemove(x, self.data, 2).data