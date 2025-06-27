from os import system
if system("clear") != 0: system("cls")


import re
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)
# <span class="rc-prices-fullprice" data-autom="full-price">1.199,00 €</span>

if response.status_code == 200:
    print("La peticion fue exitosa")

    html = response.text
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'

    match = re.search(price_pattern, html)

    if match:
        print(f"El precio del Macbook Air es: {match.group(1)}")
    
    
