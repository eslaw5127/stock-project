from email.charset import BASE64
import requests

#https://www.alphavantage.co/documentation/

API_KEY = '8E1LCLI81IQHDHAY'
BASE_URL = 'https://www.alphavantage.co/query'
function = "CURRENCY_EXCHANGE_RATE"
from_currency = "ETH"
to_currency = "USD"

request_url = f'{BASE_URL}?function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}'
response = requests.get(request_url)

data = response.json()
print(data)