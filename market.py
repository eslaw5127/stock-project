from stock_class import Stock
from stock_class import Crypto
from email.charset import BASE64
import requests

API_KEY = '8E1LCLI81IQHDHAY'
BASE_URL = 'https://www.alphavantage.co/query'

print("Welcome to Evan's Stock Viewer\n")
print("Would you like to view cryptocurrency (c) or stocks (s)? ")
option = input("Which option would you like to choose? ")

while(option != 'c' and option != 's'):
    print("Invalid input please try again")
    print("Would you like to view cryptocurrency (c) or stocks (s)? ")
    option = input("Which option would you like to choose? ")

if option == 's':
    symbol = input("\nWhat is the symbol of the stock? ")

    request_url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(request_url)

    data = response.json()
    if list(data)[0] == "Error Message":
        print("Invalid symbol please try again")
        symbol = input("\nWhat is the symbol of the stock? ")

        request_url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(request_url)

        data = response.json()
    
    today_data = list(data["Time Series (Daily)"].values())[0]

    open = round(float(list(today_data.values())[0]),2)
    high = round(float(list(today_data.values())[1]),2)
    low = round(float(list(today_data.values())[2]),2)
    close = round(float(list(today_data.values())[3]),2)

    


