from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
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

    order = relationship(
        "Order",
        back_populates = "order_items"
    )

    product = relationship(
        "Product",
        back_populates = "order_items"
    )

    