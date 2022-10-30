import requests
import json
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_Price = response.json()
    bitcoin_Price = bitcoin_Price["bpi"]
    bitcoin_Price = bitcoin_Price["USD"]
    bitcoin_Price = float((bitcoin_Price["rate"].replace(",", "")))
    quantity = float(sys.argv[1])
    price = "{:,.4f}".format(bitcoin_Price * quantity, ".4f")
    print("$" + price)
except (requests.RequestException, IndexError):
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
