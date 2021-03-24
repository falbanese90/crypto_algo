"""Retrieves Technical analysis and creates Class."""
import pandas as pd
import pandas_ta as ta
from Historic_Crypto import HistoricalData

df = HistoricalData('BTC-USD', 86400, '2020-06-01-00-00').retrieve_data()
"""This will eventually be condensed and used a year to date param."""

CustomStrategy = ta.Strategy(name='Simple Moving',
                             description='SMA 50',
                             ta=[{'kind': 'sma', 'length': 50}])
"""Simply add the SMA 50 to dataframe."""

df.ta.strategy(CustomStrategy)
df = df.tail()

class Technicals():
    """Create attributes based on technical analysis."""

    def __init__(self, df):
        """Price and sma50 attributes."""
        self.price = df['open'][-1]
        self.fifty = df['SMA_50'][-1]

    @property
    def percent_over_fifty(self):
        """Grab the percentage over 50 day MA."""
        round((((self.price - self.fifty) / self.price) * 100), 2)
