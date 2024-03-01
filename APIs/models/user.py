from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from pydantic import BaseModel

class ProductCreate(BaseModel):
    supplier_ids: int
    product_code: str
    product_name: str
    description: str
    standard_cost: float
    list_price: float
    reorder_level: int
    target_level: int
    quantity_per_unit: str
    discontinued: int
    minimum_reorder_quantity: int
    category: str
    attachments: str


class products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    supplier_ids = Column(Integer)
    product_code = Column(String)
    product_name = Column(String)
    description = Column(String)
    standard_cost = Column(Float)
    list_price = Column(Float)
    reorder_level = Column(Integer)
    target_level = Column(Integer)
    quantity_per_unit = Column(Integer)
    discontinued = Column(Integer)
    minimum_reorder_quantity = Column(Integer)
    category = Column(String)
    attachments = Column(String)



class Orders(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    ship_city = Column(String)
    ship_state_province	= Column(String)
    city_count = Column(Integer)