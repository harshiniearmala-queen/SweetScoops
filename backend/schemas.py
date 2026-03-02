from pydantic import BaseModel
from datetime import datetime


# Schema for creating new ice cream
class IceCreamCreate(BaseModel):
    name: str
    flavor: str
    price: float
    stock: int

class IceCreamUpdate(BaseModel):
    name: str
    flavor: str
    price: float
    stock: int  

class ProductCreate(BaseModel):
    name: str
    flavor: str
    price: float
    stock: int


class ProductResponse(ProductCreate):
    id: int
    created_at: datetime


# Schema for returning ice cream data
class IceCreamResponse(BaseModel):
    id: int
    name: str
    flavor: str
    price: float
    stock: int
    created_at: datetime  # Optional: ISO timestamp

    class Config:
        from_attributes = True  # Allows returning SQLAlchemy models directly