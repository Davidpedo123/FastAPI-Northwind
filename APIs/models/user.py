from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    attachments = Column(String)  # Si los adjuntos son archivos, podrías necesitar manejarlos de manera diferente
