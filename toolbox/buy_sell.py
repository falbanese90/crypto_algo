"""Enable Buying and Selling Bitcoin."""
from coinbase.wallet.client import Client
from config.config import coin_api, coin_secret, btc_id, eth_id


def Buy():
    """Buy Bitcoin a specified Dollar amount."""
    client = Client(coin_api, coin_secret)
    balance = float(client.get_account(btc_id)['native_balance']['amount'])
    amount = round((.1 * balance), 2)
    client.buy(btc_id, amount, currency='USD')
    print(f"Buy order executed in the amount of ${amount}.")


def Sell():
    """Sell Bitcoin a specified Dollar amount."""
    client = Client(coin_api, coin_secret)
    balance = float(client.get_account(btc_id)['native_balance']['amount'])
    amount = round((.1 * balance), 2)
    client.sell(btc_id, amount, currency='USD')
    print(f"Sell order executed in the amount of ${amount}.")
