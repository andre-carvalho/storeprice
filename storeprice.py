import postgresdb
import time
import sys
import os
from libbitcointoyou.bitcointoyou import API

class AppStoreError(BaseException):
    """Exception raised for errors in the app store operations.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class appStore:

    def __init__(self):
        # default sleep time (60 seconds)
        self.sleepTime = os.getenv('SAMPLE_TIME', 60)
        self.sleepTimeBackup = None
        self.btc = API()

    def storeTransactions(self):
        try:
            orders = self.btc.OrderBook()

            if orders is not None:
                try:
                    asks = ''
                    bids = ''
                    for i in range(len(orders['asks'])):
                        if i < 150:
                            asks = asks + ( ',' if asks else '' ) + ( ( (str(orders['asks'][i])).replace('[','{') ).replace(']','}') )
                    for i in range(len(orders['bids'])):
                        if i < 150:
                            bids = bids + ( ',' if bids else '' ) + ( ( (str(orders['bids'][i])).replace('[','{') ).replace(']','}') )
                    asks = '{' + asks + '}'
                    bids = '{' + bids + '}'
                    orders = {}
                    orders['asks'] = asks
                    orders['bids'] = bids
                    db = postgresdb.bitcoinDAO()
                    db.connect()
                    db.insertOrders(orders)
                except Exception as error:
                    print(error)
                    print('The database connect parameters are ok?')
                finally:
                    db.close()

        except Exception as error:
            print(error)
            self.sleepTimeBackup = self.sleepTime
            self.sleepTime = 10
            """raise AppStoreError('Function: storeTransactions','failure on get orders from API')"""


    def storeTicker(self):
        try:
            tick = self.btc.Ticker()

            if tick is not None:
                try:
                    db = postgresdb.bitcoinDAO()
                    db.connect()
                    db.insertTicker(tick)
                except Exception as error:
                    print(error)
                    print('The database connect parameters are ok?')
                finally:
                    db.close()

        except Exception as error:
            print(error)
            self.sleepTimeBackup = self.sleepTime
            self.sleepTime = 10
            """raise AppStoreError('Function: storeTicker','failure on get ticker from API')"""
    
    def run(self):
        while True:
            self.storeTicker()
            time.sleep(1)
            self.storeTransactions()
            time.sleep(self.sleepTime)
            if self.sleepTimeBackup is not None:
                self.sleepTime = self.sleepTimeBackup
                self.sleepTimeBackup = None

if __name__ == "__main__":
    app = appStore()
    app.run()