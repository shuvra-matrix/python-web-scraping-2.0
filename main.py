from bs4 import BeautifulSoup
import requests
import lxml

PRODUCT_URL = "https://leadsquared.com/empowering-organizations-with-the-power-of-high-velocity-sales/"
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",'Accept-Language':"en-US,en;q=0.9"}

request = requests.get(PRODUCT_URL,headers=header)
supe = BeautifulSoup(request.content,'lxml')
price = supe.find('title')

other = supe.find('meta' , property="og:description")
real_price = price.get_text().lower()
other = other['content'].lower()
print(other)
print(real_price)