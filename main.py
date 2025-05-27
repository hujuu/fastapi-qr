import asyncio

import httpx
import requests
import json
from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User, get_books_by_category, Book
from book_schemas import BookSchema, BookResponseSchema
app = FastAPI()

async def fetch_address(zipcode: str):
    """Fetch address information based on zipcode."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}",
            params={"zipcode": zipcode}
        )
        return response.json()


books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, title="1984", category="Fiction"),
    BookResponseSchema(id=2, title="To Kill a Mockingbird", category="Fiction"),
    BookResponseSchema(id=3, title="The Great Gatsby", category="Fiction"),
    BookResponseSchema(id=4, title="A Brief History of Time", category="Science"),
    BookResponseSchema(id=5, title="The Selfish Gene", category="Science")
]

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

@app.get("/books/")
async def read_books(category: Optional[str] = None) -> list[dict[str, str]]:
    """Retrieve books, optionally filtered by category."""
    books = get_books_by_category(category)
    return [{"id": book.id, "title": book.title, "category": book.category} for book in books]


@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book


@app.get("/book/", response_model=list[BookResponseSchema])
def read_book():
    return books


@app.get("/address/")
async def read_address():
    zipcodes = ["1060044", "1000001", "1500001"]
    return await asyncio.gather(*(fetch_address(zipcode) for zipcode in zipcodes))

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=1060044"

zip = "1060044"

param = {"zipcode": zip}

res = requests.get(url, params=param)

data = json.loads(res.text)

if data['results'] is not None:
    address_info = data['results'][0]
    zipcode = address_info['zipcode']
    address = f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
    print(f"Zipcode: {zipcode} - Address: {address}")
else:
    print("No results")
