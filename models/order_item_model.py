from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from database.db import Base

class OrderItem(Base):

    __tablename__  = "order_items"

    id = Column(
        Integer, 
        primary_key = True,
        index = True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(
        Integer,
        nullable = False
    )

    