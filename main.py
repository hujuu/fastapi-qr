import requests
import json
from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Zipcode API"}

@app.get("/user/{user_id}")
async def read_user(user_id: int) -> dict:
    """Retrieve user information by user ID."""
    user: Optional[User] = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name}

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=1060044"

zip = "1060044"

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
