import pickle
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
import os

os.environ['IEX_TOKEN'] = 'pk_759aa8b5072941d492b68473dc97224c '

class DataReader:
    def __init__(self, symbol, start, end):
        self.data = {}
        self.symbol = symbol
        try:
            print("Loading Data from file")
            self.data = self.loadData(symbol + ".dat")
        except FileNotFoundError:
            print("Retrieving new data from IEX")
            # start = datetime(2016, 1, 1)
            # end = datetime(2021, 9, 13)
            self.data = get_historical_data(symbol, start, end, output_format='pandas')
            self.storeData(symbol + ".dat", self.data)

    def storeData(self, filename, data):    
        dbfile = open(filename, 'ab')
        pickle.dump(data, dbfile)                     
        dbfile.close()
    
    def loadData(self, filename):
        dbfile = open(filename, 'rb')     
        self.data = pickle.load(dbfile)
        dbfile.close()
        return self.data