import bitcointoyou
import postgresdb
import time

"""
select tb1.id, tb1.last, tb2.sample_date, tb2.sample_time from (
select max(bitcoin_price_id) as id, last from bitcoin_price group by last
) as tb1, (
select bitcoin_price_id as id, sample_time, sample_date from bitcoin_price) as tb2
where tb1.id=tb2.id
order by tb2.sample_date, tb2.sample_time
"""

def app():
    api_key = ''
    api_pass = ''

    btc = bitcointoyou.API(api_key, api_pass)
    def getTicker():
        tick = btc.Ticker() 
        if tick is not None:
            db = postgresdb.bitcoinDAO()
            db.connect()
            db.insertData(tick)
            db.close()
        time.sleep(60)
    
    while True:
        getTicker()

if __name__ == "__main__":
    app()