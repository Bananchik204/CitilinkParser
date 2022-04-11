from bs4 import BeautifulSoup
import requests

url = "https://www.citilink.ru/catalog/noutbuki/?text=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8&f=discount.any%2Crating.any&price_max=55000&pf=discount.any%2Crating.any"
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")

notebook_name = bs.find_all("a", class_="ProductCardHorizontal__title", href=True)
notebook_price = bs.find_all("span", class_="ProductCardHorizontal__price_current-price")

for notebook in notebook_name:
	print(f"Name: {notebook.text}")
	print("https://www.citilink.ru" + notebook['href'])