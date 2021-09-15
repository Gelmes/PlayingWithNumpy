import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import math
from matplotlib.widgets import Slider, Button
from dataReader import DataReader
from polyRemove import PolyRemove

dataFrame = DataReader("SPY", 
            datetime(2016, 1, 1), 
            datetime(2021, 9, 13))
closePrices = dataFrame.data['close'].to_numpy(dtype=float)

width = 16
size = closePrices.size
remainder = math.floor(size / width)
print(size, remainder, width*remainder)
copy = closePrices[0:remainder*width].reshape(width, remainder)

print(type(copy))
myImage = plt.imshow(copy, aspect="auto", interpolation='nearest')

init_amplitude = 5
# axamp = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow')
axamp = plt.axes([0.03, 0.11, 0.02, 0.77], facecolor='lightgoldenrodyellow')
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=1,
    valmax=(closePrices.size / 10),
    valinit=init_amplitude,
    orientation="vertical"
)

def update(val):
    width = math.floor(val)
    size = closePrices.size
    remainder = math.floor(size / width)
    print(size, remainder, width*remainder)
    copy = closePrices[0:remainder*width].reshape(width, remainder)
    myImage.set_data(copy)
    # draw()
amp_slider.on_changed(update)


#############################
# Data plot
# plt.figure(figsize=(10,10))
x = mdates.date2num(dataFrame.data.index)

polyArray = PolyRemove(x, closePrices, 1).data
plt.plot(x, closePrices, label="close")
plt.plot(x, polyArray, label="poly")
plt.plot(x, closePrices-polyArray, label="normalized")
plt.legend()

plt.show()
quit()