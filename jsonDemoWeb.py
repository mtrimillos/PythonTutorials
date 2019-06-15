import json
from urllib.request import urlopen

# currently, yahoo finance is down
# with urlopen(
#     "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
# ) as response:
#     source = response.read()

with urlopen("https://cart.lazada.com.ph/cart/api/count") as response:
    source = response.read()

print(source)
