import postgresdb
import time
import sys
import os

base_dir = os.path.dirname(__file__) or '.'
# Insert the libbitcointoyou directory at the front of the path.
libbitcointoyou = os.path.join(base_dir, 'libbitcointoyou')
sys.path.insert(0, libbitcointoyou)
import bitcointoyou

def app():
    api_key = ''
    api_pass = ''

    btc = bitcointoyou.API(api_key, api_pass)
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