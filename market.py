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

if option == 'c':
    print("Crypto")