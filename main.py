import requests
import json

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=1060044"

zip = input("Enter zipcode: ")

param = {"zipcode": zip}

res = requests.get(url, params=param)

data = json.loads(res.text)

print(data)

print('*' * 50)

if data['results'] is not None:
    address_info = data['results'][0]
    zipcode = address_info['zipcode']
    address = f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
    print(f"Zipcode: {zipcode} - Address: {address}")
else:
    print("No results")
