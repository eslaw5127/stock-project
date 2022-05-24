'''
This is test code for the main market program

-The purpose of this code is to get the correct data from the API
-This code implements the alphavantage APIs for stocks
-Daily information on the stock

Documentation for the API
https://www.alphavantage.co/documentation/

'''

from email.charset import BASE64
import requests
from datetime import date


API_KEY = '8E1LCLI81IQHDHAY'
BASE_URL = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'

symbol = input("Please enter a symbol: ")

#Daily API
request_url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
response = requests.get(request_url)

today = date.today()
print("Today's date:", today)

data = response.json()
today_data = list(data["Time Series (Daily)"].values())[0]

open = round(float(list(today_data.values())[0]),2)
print("Today's Open: " , open)
high = round(float(list(today_data.values())[1]),2)
print("Today's High: " , high)
low = round(float(list(today_data.values())[2]),2)
print("Today's Low: " , low)
close = round(float(list(today_data.values())[3]),2)
print("Today's close: " , close)


#Quote Endpoint API
url_new = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
r_new = requests.get(url_new)
data_new = r_new.json()

data_new = data_new['Global Quote']
print(data_new)

price = data_new["05. price"]
change = data_new["09. change"]
change_percent = data_new["10. change percent"]

print("Today's Price: " , price)
print("Today's Change: " , change)
print("Today's Percent Change: " , change_percent)

