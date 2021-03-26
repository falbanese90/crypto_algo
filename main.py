"""Execute Algo."""
from chart_maker import year_to_date
from get_technicals import Technicals
from buy_sell import Buy, Sell
import time

if __name__ == '__main__':
    while True:
        btc = year_to_date()
        btc = Technicals(btc)
        if btc.sell:
            Sell()
            time.sleep(86400)
        elif btc.buy:
            Buy()
            time.sleep(86400)
        else:
            time.sleep(10800)
