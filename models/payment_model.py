from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base

class Payment(Base):

    __tablename__ = "payments"

    id = Column(
        Integer, 
        primary_key = True, 
        index = True
    )

    order_id = Column(
        Integer, 
        ForeignKey("orders.id")
    )

    amount = Column(
        Integer, 
        nullable = False
    )

    status = Column(
        String(50), 
        nullable = False
    )

    order = relationship(
        "Order", 
        back_populates = "payment"
    )

    