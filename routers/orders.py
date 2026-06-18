from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.db import SessionLocal

from models.order_model import Order
from models.order_item_model import OrderItem
from models.product_model import Product

from schemas.order_schema import OrderCreate
from schemas.order_schema import OrderResponse
from services.auth_service import get_current_user




router = APIRouter(
    prefix = "/orders",
    tags = ["Orders"]
)

def get_db():

    db = SessionLocal()

    try: 
        yield db
    
    finally:

        db.close()


@router.post(
    "/",
    response_model = OrderResponse
)
def create_order(
    order : OrderCreate,
    current_user = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    total_amount = 0

    for item in order.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            
            raise HTTPException(
                status_code = 404,
                detail = f"Product {item.product_id} Not Found!"
            )
        
        if product.stock < item.quantity:
            raise HTTPException(
                status_code = 400, 
                detail = f"Insufficient stock for {product.name}"
            )
        
        total_amount += (
            product.price * item.quantity
        )

    
    new_order = Order(
        user_id = current_user.id,
        total_amount = total_amount
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)


    for item in order.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        order_item = OrderItem(
            order_id = new_order.id,
            product_id = item.product_id,
            quantity = item.quantity
        )

        db.add(order_item)

        product.stock -= item.quantity

    db.commit()

    return new_order


