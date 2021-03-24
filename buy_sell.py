"""Enable Buying and Selling Bitcoin."""
from coinbase.wallet.client import Client
from config.config import coin_api, coin_secret, btc_id, eth_id

client = Client(coin_api, coin_secret)

def Buy(amount):
    """Buy Bitcoin a specified Dollar amount."""
    client.buy(btc_id, amount=amount, currency='USD')

def Sell(amount):
    """Sell Bitcoin a specified Dollar amount."""
    client.buy(btc_id, amount=amount, currency='USD')
