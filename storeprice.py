import postgresdb
import time
import sys
import os
from libbitcointoyou.bitcointoyou import API

def app():
    api_key = ''
    api_pass = ''

    btc = API(api_key, api_pass)
    def getTicker():
        # default sleep time (60 seconds)
        t = os.getenv('SAMPLE_TIME', 60)

        try:
            tick = btc.Ticker()

            if tick is not None:
                try:
                    db = postgresdb.bitcoinDAO()
                    db.connect()
                    db.insertData(tick)
                except Exception as error:
                    print(error)
                    print('The database connect parameters are ok?')
                finally:
                    db.close()

        except Exception as error:
            print(error)
            # less time to retry
            t = 10
        
        time.sleep(t)
    
    while True:
        getTicker()

if __name__ == "__main__":
    app()