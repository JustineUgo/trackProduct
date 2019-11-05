from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


website_connection = Request("https://www.jumia.com.ng/catalog/?q=flexible+phone+holder", headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(website_connection).read()

#bs4 object
soup = BeautifulSoup(webpage, 'html.parser')

#section of products
main_content = soup.find(class_="products -mabaya")

#list prices of all items
prices = main_content.find_all(class_="price")
for price in prices:
    print(price.get_text())
print(len(main_content))
