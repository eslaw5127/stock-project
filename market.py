from stock_class import Stock
from stock_class import Crypto
from email.charset import BASE64
import requests

API_KEY = '8E1LCLI81IQHDHAY'
BASE_URL = 'https://www.alphavantage.co/query'

print("Welcome to Evan's Stock Viewer\n")


continue_var = "yes"
while continue_var != "no":
    #main list to hold all of the stocks viewed
    main_list = []

    print("Would you like to view cryptocurrency (c) or stocks (s)? ")
    option = input("Which option would you like to choose? ")

    #check for valid input
    while(option != 'c' and option != 's'):
        print("Invalid input please try again")
        print("Would you like to view cryptocurrency (c) or stocks (s)? ")
        option = input("Which option would you like to choose? ")

    
    #option for stocks
    if option == 's':
        symbol = input("\nWhat is the symbol of the stock? ")

        request_url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(request_url)

        data = response.json()

        #checking to make sure the symbol is valid
        while list(data)[0] == "Error Message":
            print("Invalid symbol please try again")
            symbol = input("\nWhat is the symbol of the stock? ")

            url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

            response = requests.get(url)
            data = response.json()

        #symbol is valid and continuing
        open,close,high,low = Stock.time_series_daily(symbol)
        price,change,change_percent = Stock.global_quote(symbol)
        
        #initalize the stock with the values needed
        stock = Stock(symbol,open,close,high,low,price,change,change_percent)
        main_list.append(stock)
        
        stock.print_data()

    if option == "c":
        symbol = input("What is the symbol for the cryptocurrency? ")
        
        url = f'{BASE_URL}?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency=USD&apikey={API_KEY}'
        response = requests.get(url)

        data = response.json()
        while list(data)[0] == "Error Message":
            print("Invalid symbol please try again")
            symbol = input("\nWhat is the symbol of the cryptocurrency? ")

            url = f'{BASE_URL}?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency=USD&apikey={API_KEY}'

            response = requests.get(url)
            data = response.json()

        price,name = Crypto.crypto_rates(symbol)
        crypto = Crypto(symbol,price,name)

        main_list.append(crypto)

        crypto.print_crypto()


    continue_var = input("Would you like to to view another? (yes/no) ")       



