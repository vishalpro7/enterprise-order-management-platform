from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from database.db import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key = True, index = True)

    name = Column(String(300), nullable = False)

    description = Column(String(500))

    price = Column(Integer, nullable = False)

    stock = Column(Integer, nullable = False)

    
