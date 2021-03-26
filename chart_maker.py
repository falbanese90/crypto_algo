from Historic_Crypto import HistoricalData
import time
import pandas as pd
import datetime

year_ago = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime('%Y-%m-%d-%H-%M')

def year_to_date(currency='BTC-USD'):
    df = HistoricalData(currency, 86400, year_ago).retrieve_data()
    time.sleep(3)
    df['sma_50'] = df['close'].rolling(50).mean()
    return df
