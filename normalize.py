import pandas as pd
class Normal:
    def __init__(self, data):
        if (type(data) == pd.core.frame.DataFrame):
            self.dataFrame = data
        else:
            self.dataFrame = pd.DataFrame(data)
        # self.data = ( (self.dataFrame-self.dataFrame.mean())/self.dataFrame.std() ).values
        self.data = ( (self.dataFrame-self.dataFrame.min())/(self.dataFrame.max()-self.dataFrame.min()) ).values
        print(self.data)