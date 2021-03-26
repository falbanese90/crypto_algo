"""Execute Algo."""
from toolbox.chart_maker import year_to_date
from toolbox.get_technicals import Technicals
from toolbox.buy_sell import Buy, Sell
import time


def algo_loop():
    """Execute the algo loop. Currently disables Buys and Sells."""
    x = 0
    trigger = 40
    while x < 3:
        btc = year_to_date()
        btc = Technicals(btc, trigger)
        if btc.sell:
            """Sell()"""
            print("Sell!")
            trigger *= .2
            print(f'Trigger is now {trigger}%')
            time.sleep(86400)
        elif btc.buy:
            """Buy()"""
            print("Buy!")
            x += 1
            time.sleep(86400)
        else:
            print("Waiting..")
            time.sleep(10800)


if __name__ == '__main__':
    algo_loop()
