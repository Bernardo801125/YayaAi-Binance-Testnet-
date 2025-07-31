import time
import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='com', testnet=True)
client.API_URL = config.BASE_URL

print("Conexión exitosa a Binance Testnet.")
balance = client.get_asset_balance(asset='USDT')
print("Balance USDT:", balance)