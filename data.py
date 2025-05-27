from typing import Optional

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Book:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category

user_list = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob"),
    User(id=3, name="Charlie")
]

book_list = [
    Book(id="1", title="1984", category="Fiction"),
    Book(id="2", title="To Kill a Mockingbird", category="Fiction"),
    Book(id="3", title="The Great Gatsby", category="Fiction"),
    Book(id="4", title="A Brief History of Time", category="Science"),
    Book(id="5", title="The Selfish Gene", category="Science")
]

def get_user(user_id: int) -> Optional[User]:
    """Retrieve a user by ID."""
    for user in user_list:
        if user.id == user_id:
            return user
    return None

def get_books_by_category(category: Optional[str] = None) -> list[Book]:
    """Retrieve books by category."""
    if category is None:
        return book_list
    else:
        return [book for book in book_list if book.category.lower() == category.lower()]
