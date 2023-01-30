import requests
url = 'https://api.coingecko.com/api/v3/coins/dogecoin/history?date=30-01-2023&localization=false'
response = requests.get(url)

print(response.json())


def get_custom_rate(coin: str, exchange: str, period: str):
    pass