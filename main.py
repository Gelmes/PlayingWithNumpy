import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from iexfinance.stocks import get_historical_data
import numpy as np
import pickle
import math

def storeData(filename, data):      
    # Its important to use binary mode
    dbfile = open(filename, 'ab')
      
    # source, destination
    pickle.dump(data, dbfile)                     
    dbfile.close()
  
def loadData(filename):
    # for reading also binary mode is important
    dbfile = open(filename, 'rb')     
    data = pickle.load(dbfile)
    dbfile.close()
    return data

start = datetime(2016, 1, 1)
end = datetime(2021, 9, 13)

df = {}
symbol = "SPY"
try:
    print("Loading Data from file")
    df = loadData(symbol + ".dat")
except FileNotFoundError:
    print("Retrieving new data")
    df = get_historical_data(symbol, start, end, output_format='pandas')
    storeData(symbol + ".dat", df)

# print(df['close'].size)
# data = df['close'].values[0:600].reshape(200,3)
data = df['close'].to_numpy(dtype=float)

width = 16
size = data.size
remainder = math.floor(size / width)
print(size, remainder, width*remainder)
copy = data[0:remainder*width].reshape(width, remainder)
# copy = np.array(data, dtype=float)

print(copy.shape)


# print(data.size)
# pd.DataFrame(data).to_csv("out.csv")
# data = np.random.normal(0,1,size=[100,100])
# print(data)
print(type(copy))
plt.imshow(copy, aspect="auto", interpolation='nearest')
# plt.show()

df["SMA1"] = df['close'].rolling(window=50).mean()
df["SMA2"] = df['close'].rolling(window=200).mean()
df['ewma'] = df['close'].ewm(halflife=0.5, min_periods=20).mean()
# print(df.index)

print(len(df.index))
print(len(df['close'].to_numpy(dtype=float)))

x = mdates.date2num(df.index)
z = np.polyfit(x, df['close'].to_numpy(dtype=float), 1)
p = np.poly1d(z)
# plt.plot(p)

plt.figure(figsize=(10,10))
# plt.plot(df['SMA1'], 'g--', label="SMA1")
# plt.plot(df['SMA2'], 'r--', label="SMA2")
# plt.plot(df['close'], label="close")

data = df['close'].to_numpy(dtype=float)
plt.plot(x, data, label="close")
plt.plot(p.linspace(len(data), [x[0], x[-1]]), label="poly")
plt.legend()
plt.show()
quit()

# df['close'].values.reshape()

plt.figure(figsize=(10,10))
plt.plot(df.index, df['close'])
plt.xlabel("date")
plt.ylabel("$ price")
plt.title("DIS Stock Price 1/1/17 - 8/1/19")

df["SMA1"] = df['close'].rolling(window=50).mean()
df["SMA2"] = df['close'].rolling(window=200).mean()
df['ewma'] = df['close'].ewm(halflife=0.5, min_periods=20).mean()
plt.figure(figsize=(10,10))
plt.plot(df['SMA1'], 'g--', label="SMA1")
plt.plot(df['SMA2'], 'r--', label="SMA2")
plt.plot(df['close'], label="close")
plt.legend()
plt.show()

df['middle_band'] = df['close'].rolling(window=20).mean()
df['upper_band'] = df['close'].rolling(window=20).mean() + df['close'].rolling(window=20).std()*2
df['lower_band'] = df['close'].rolling(window=20).mean() - df['close'].rolling(window=20).std()*2
plt.figure(figsize=(10,10))
plt.plot(df['upper_band'], 'g--', label="upper")
plt.plot(df['middle_band'], 'r--', label="middle")
plt.plot(df['lower_band'], 'y--', label="lower")
plt.plot(df['close'], label="close")
plt.legend()
plt.show()
plt.figure(figsize=(10,10))
plt.plot(df['upper_band'].iloc[-200:], 'g--', label="upper")
plt.plot(df['middle_band'].iloc[-200:], 'r--', label="middle")
plt.plot(df['lower_band'].iloc[-200:], 'y--', label="lower")
plt.plot(df['close'].iloc[-200:], label="close")
plt.legend()
plt.show()