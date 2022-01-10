from tkinter import *
from PIL import ImageTk, Image
import os
from binance.client import Client

#init
api_key = '3slksxolZo2WhDXAZ6vwCkSqstMqs9SYBsDNAnYWxSHrzMumsz65hi2iCWjFkhwI'
api_secret = 'nkTkXBHdttowlwMVnvQQFbyVB01VB7RRXDtdLR5npXixv3gh5TvB4Fie6Zy9uZhm'
#api_key = os.environ.get('binance_api')
#api_secret = os.environ.get('binance_secret')

# create main window
root = Tk()
root.title('Binance app') #main window title
root.iconbitmap('quakechamps.ico') #main window icon
root.geometry("400x400") #main window size

# connect to the api
client = Client(api_key, api_secret)
client.API_URL = 'https://api1.binance.com/api'

# get balances for assets
print(client.get_asset_balance(asset='USDT'))
print(client.get_asset_balance(asset='VITE'))
print(client.get_asset_balance(asset='SXP'))
print(client.get_asset_balance(asset='DENT'))

# get latest price
chr_price = client.get_symbol_ticker(symbol='CHRUSDT')
# print full output (dictionary)
print(chr_price)
# print just the price
print(chr_price["price"])




#try:
#    api_request = requests.get("http://")
#    api = json.loads(api_request.content)
#except Exception as e:
#    api = "Error..."

#label = Label(root, text=api)
#label.pack()

root.mainloop()
