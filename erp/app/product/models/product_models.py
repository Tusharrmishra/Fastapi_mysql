# models.py

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    unit_price = Column(Float)
    cost_price = Column(Float)
    quantity_on_hand = Column(Integer)
    reorder_level = Column(Integer)

