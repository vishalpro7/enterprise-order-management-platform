from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from models.order_model import Order
from models.order_item_model import OrderItem
from models.product_model import Product

from schemas.order_schema import OrderCreate
from schemas.order_schema import OrderResponse




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


@router.post("/", response_model = OrderResponse)
def create_order(
    order : OrderCreate,
    db : Session = Depends(get_db)
):
    return {
        "id" : 1,
        "user_id" : 2,
        "total_amount" : 100
    }