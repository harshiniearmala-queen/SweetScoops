# backend/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, get_db
from models import IceCream, Product
from schemas import (
    IceCreamCreate,
    IceCreamResponse,
    IceCreamUpdate,
    ProductCreate,
    ProductResponse
)

import crud


# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="SweetScoops IceCream API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# ROOT
# ==============================
@app.get("/")
def root():
    return {"message": "SweetScoops API is running 🍦"}


# ==============================
# LOGIN (Simple Hardcoded Auth)
# ==============================
class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "1234":
        return {
            "access_token": "fake-token",
            "token_type": "bearer"
        }
    else:
        return {"error": "Invalid credentials"}


# ==============================
# ICECREAMS
# ==============================
@app.get("/icecreams", response_model=list[IceCreamResponse])
def read_icecreams(db: Session = Depends(get_db)):
    return crud.get_icecreams(db)


@app.post("/icecreams", response_model=IceCreamResponse)
def add_icecream(icecream: IceCreamCreate, db: Session = Depends(get_db)):
    return crud.create_icecream(db, icecream)


@app.put("/icecreams/{icecream_id}", response_model=IceCreamResponse)
def update_icecream(
    icecream_id: int,
    icecream: IceCreamUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_icecream(db, icecream_id, icecream)
    if not updated:
        return {"error": "IceCream not found"}
    return updated


# ==============================
# PRODUCTS
# ==============================
@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}