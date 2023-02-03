import requests
import os
from pprint import pprint

ENDPOINT = "/asset_platforms"
ENDPOINT = "/coins/categories/list"
URL = "https://api.coingecko.com/api/v3"

endpoint = URL + ENDPOINT
print("Endpoint:", endpoint)
response = requests.get(
    endpoint,
    verify=False,
)

if response.status_code == requests.codes.OK:
    # print(response.content)
    # print("-" * 60)
    data = response.json()
    # pprint(data)
    for coin in data:
        print(coin)

    print()
    for key, value in sorted(response.headers.items()):
        print(key, value)
else:
    print("SORRY, INVALID REQUEST")