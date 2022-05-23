from email.charset import BASE64
import requests
from datetime import date

#https://www.alphavantage.co/documentation/

API_KEY = '8E1LCLI81IQHDHAY'
BASE_URL = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'

symbol = input("Please enter a symbol: ")

request_url = f'{BASE_URL}?function={function}&symbol={symbol}&apikey={API_KEY}'
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

print("Daily performace:" , round((close-open),2) , "(" + str(round((close/open),2)) + "%)")

url_new = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NIO&apikey={API_KEY}'
r_new = requests.get(url_new)
data_new = r_new.json()

print(data_new)