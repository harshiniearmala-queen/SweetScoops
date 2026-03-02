from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from database import Base

class IceCream(Base):
    __tablename__ = "icecreams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    flavor = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    flavor = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)