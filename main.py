
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
from matplotlib.widgets import Slider
from dataReader import DataReader
from polyRemove import PolyRemove
from expRemove import ExpRemove
from sma import SMA
from normalize import Normal
from multiPolyRemove import MultiPolyRemove

dataFrame = DataReader("DIS", 
            datetime(2019, 1, 1), 
            datetime(2021, 9, 13))

closePrices = dataFrame.data['close'].to_numpy(dtype=float)
x = mdates.date2num(dataFrame.data.index)
multiPolyRemove = MultiPolyRemove(x, closePrices, samples=10)
pricesPolyFiltered = PolyRemove(x, closePrices, 2)
pricesPolyFiltered2 = PolyRemove(x, pricesPolyFiltered.data, 2)
pricesPolyFiltered3 = PolyRemove(x, pricesPolyFiltered2.data, 2)
# pricesExpFiltered = ExpRemove(x, closePrices, 1)
pricesSMA = SMA(multiPolyRemove.data,3).data
normal = Normal(pricesPolyFiltered.data).data


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
plt.plot(x, pricesPolyFiltered.array, label="poly")
plt.plot(x, pricesPolyFiltered2.array, label="poly2")
plt.plot(x, pricesPolyFiltered3.array, label="poly3")
plt.plot(x, multiPolyRemove.data, label="multi")
plt.plot(x, pricesSMA, label="poly sma")
plt.legend()

plt.figure(figsize=(10,10))
plt.plot(x, normal, label="normal")
plt.legend()

plt.show()
quit()