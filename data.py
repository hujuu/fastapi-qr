from typing import Optional

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

user_list = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob"),
    User(id=3, name="Charlie")
]

def get_user(user_id: int) -> Optional[User]:
    """Retrieve a user by ID."""
    for user in user_list:
        if user.id == user_id:
            return user
    return None
