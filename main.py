from chart_maker import year_to_date
from get_technicals import Technicals
from buy_sell import Buy, Sell

if __name__ == '__main__':
    btc = year_to_date()
    btc = Technicals(btc)

    if btc.sell:
        """Sell(100)"""
    elif btc.buy:
        """Buy(100)"""
    else:
        pass
