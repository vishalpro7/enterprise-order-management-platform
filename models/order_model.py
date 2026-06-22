from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
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
    
    user = relationship(
        "User",
        back_populates = "orders"
    )

    order_items = relationship(
        "OrderItem",
        back_populates = "order"
    )

    
    