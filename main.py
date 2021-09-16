import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import math
from matplotlib.widgets import Slider, Button
from dataReader import DataReader
from polyRemove import PolyRemove
from sma import SMA

dataFrame = DataReader("SPY", 
            datetime(2019, 1, 1), 
            datetime(2021, 9, 13))

closePrices = dataFrame.data['close'].to_numpy(dtype=float)
x = mdates.date2num(dataFrame.data.index)
pricesPolyFiltered = PolyRemove(x, closePrices, 1).data
pricesSMA = SMA(pricesPolyFiltered,3).data


dataArray = pricesSMA

width = 16
size = dataArray.size
remainder = math.floor(size / width)
copy = dataArray[0:remainder*width].reshape(width, remainder)

fig, ax =  plt.subplots()
myImage = ax.imshow(copy, aspect="auto", interpolation='nearest')

init_amplitude = 5
axamp = plt.axes([0.03, 0.11, 0.02, 0.77], facecolor='lightgoldenrodyellow')
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=1,
    valmax=(dataArray.size / 10),
    valinit=init_amplitude,
    orientation="vertical"
)

def update(val):
   
    width = math.floor(val)
    size = dataArray.size
    remainder = math.floor(size / width)
    copy = dataArray[0:remainder*width].reshape(width, remainder)
    myImage.set_data(copy)
    # draw()
amp_slider.on_changed(update)


#############################
# Data plot
plt.figure(figsize=(10,10))

plt.plot(x, closePrices, label="close")
plt.plot(x, pricesPolyFiltered, label="poly")
plt.plot(x, pricesSMA, label="poly sma")
plt.legend()

plt.show()
quit()