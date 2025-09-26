from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(...)

class User(UserCreate):
    id: int

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float

class Item(ItemCreate):
    id: int