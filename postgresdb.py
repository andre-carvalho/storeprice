import psycopg2
from config import config

class ConnectionError(BaseException):
    """Exception raised for errors in the DB connection.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class bitcoinDAO:
    
    def __init__(self):
        # read connection parameters
        self.params = config()

    def connect(self):
        self.conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self.params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def close(self):
        # disconnect from the PostgreSQL server
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def createTable(self):
        table = """
            CREATE TABLE bitcoin_price (
                bitcoin_price_id SERIAL PRIMARY KEY,
                low double precision,
                vol double precision,
                buy double precision,
                buy_qty double precision,
                sell double precision,
                sell_qty double precision,
                last double precision,
                high double precision,
                sample_date date,
                sample_time time
            )"""

        try:
            if self.conn is not None:
                # create a cursor
                cur = self.conn.cursor()
            else:
                raise ConnectionError('Missing connection:', 'Has no valid database connection')
            # execute a statement
            cur.execute(table)
            # close the communication with the PostgreSQL
            cur.close()
            # commit the changes
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        except (BaseException) as error:
            print(error)

    def insertData(self, tick):
        table = """
            INSERT INTO bitcoin_price(low, vol, buy, buy_qty, sell, sell_qty, last, high, sample_date, sample_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, to_timestamp(%s)::date, to_timestamp(%s)::time)
            """

        try:
            if self.conn is not None:
                # create a cursor
                cur = self.conn.cursor()
            else:
                raise ConnectionError('Missing connection:', 'Has no valid database connection')
            # execute a statement
            cur.execute(table, (tick['ticker']['low'],tick['ticker']['vol'],tick['ticker']['buy'],
            tick['ticker']['buyQty'],tick['ticker']['sell'],tick['ticker']['sellQty'],
            tick['ticker']['last'],tick['ticker']['high'],tick['ticker']['date'],tick['ticker']['date']))
            # close the communication with the PostgreSQL
            cur.close()
            # commit the changes
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        except (BaseException) as error:
            print(error)