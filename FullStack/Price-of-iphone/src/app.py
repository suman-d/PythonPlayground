import requests
from bs4 import BeautifulSoup

request_amazon = requests.get("http://www.amazon.in/Apple-iPhone-6-Silver-16GB/dp/B00O4WTJKW?ie=UTF8&ascsubtag=1ba00-01000-org00-win70-other-nomod-in000-pcomp&tag=amz-mkt-chr-in-21")
request_flipkart = requests.get("https://www.flipkart.com/apple-iphone-6-space-grey-16-gb/p/itme8dvfeuxxbm4r?pid=MOBEYHZ2YAXZMF2J&srno=s_1_1&otracker=search&lid=LSTMOBEYHZ2YAXZMF2JEVWVNC&qH=66f7d7b18ad093cf")
request_snapdeal = requests.get("https://www.snapdeal.com/product/apple-iphone-6-16-gb/1270529654#bcrumbSearch:iphone%206")


content_amazon = request_amazon.content
content_flipkart = request_flipkart.content
content_snapdeal = request_snapdeal.content



soup_amazon = BeautifulSoup(content_amazon, "html.parser")
soup_flipkart = BeautifulSoup(content_flipkart, "html.parser")
soup_snapdeal = BeautifulSoup(content_snapdeal, "html.parser")


# Amazon : <span id="priceblock_ourprice" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span> 37,690</span>
# Flipkart : <div class="_1vC4OE _37U4_g"><!-- react-text: 9321 -->₹<!-- /react-text --><!-- react-text: 9322 -->33,990<!-- /react-text --></div>
# Snapdeal : <span class="payBlkBig" itemprop="price">36,985</span>
element_amazon = soup_amazon.find("span", {"id":"priceblock_ourprice", "class":"a-size-medium a-color-price"})
element_flipkart = soup_flipkart.find("div", {"class":"_1vC4OE _37U4_g"})
element_snapdeal = soup_snapdeal.find("span", {"class":"payBlkBig", "itemprop":"price"})



print(str(element_amazon.text).strip())
print(element_snapdeal.text)

#print(element_flipkart.text)
