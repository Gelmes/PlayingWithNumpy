import pandas as pd

class SMA:
    def __init__(self, data, window=3):
        if (type(data) == pd.core.frame.DataFrame):
            self.dataFrame = data
        else:
            self.dataFrame = pd.DataFrame(data)
        print(type(self.dataFrame))
        self.data = self.dataFrame.rolling(window=window).mean().values