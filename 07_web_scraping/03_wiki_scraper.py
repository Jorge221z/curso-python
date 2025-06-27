from os import system
if system("clear") != 0: system("cls")

from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
  }
response = requests.get(url)

if response.status_code == 200:
    print('La petición fue exitosa!')

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.prettify())
    title_tag = soup.title
    if title_tag:
        print(f"El titulo de la web es: {title_tag.string}")

    #encontrar un precio(el primero)
    # price_span = soup.find('span', class_='rc-prices-fullprice')
    # if price_span:
    #     print(f"El precio del producto es: {price_span.text}")

    #encontrar todos los precios
    # prices_span = soup.find_all('span', class_='rc-prices-fullprice')
    # for price in prices_span:
    #     print(f"El precio del producto es: {price.text}")

    products = soup.find_all(class_="rc-productselection-item")
    for product in products:
        name = product.find(class_="list-title").text
        price = product.find(class_='rc-prices-fullprice').text
        print(f"El producto {name} tiene un precio de {price}")
