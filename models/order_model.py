from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from database.db import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, 
                primary_key = True,
                index = True)
    
    user_id = Column(Integer, 
                     ForeignKey("users.id"))
    
    total_amount = Column(Integer,
                          nullable = False)
    
    