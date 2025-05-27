from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    category: str

class BookResponseSchema(BookSchema):
    id: int
