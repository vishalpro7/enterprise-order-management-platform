from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from schemas.payment_schema import PaymentResponse, PaymentCreate
from models.order_model import Order
from schemas.order_schema import OrderStatusUpdate
from models.payment_model import Payment
from services.auth_service import get_current_user

router = APIRouter(
    prefix = "/payments",
    tags = ["Payments"]
)

def get_db():

    db = SessionLocal()

    try:

        yield db
    
    finally:

        db.close()


@router.post(
        "/", 
        response_model = PaymentResponse)
def create_payment(
    payment : PaymentCreate, 
    db : Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == payment.order_id
    ).first()

    if not order:

        raise HTTPException(
            status_code = 404, 
            detail = "Order Not Found"
        )
    
    existing_payment = db.query(Payment).filter(
        Payment.order_id == order.id
    ).first()

    if existing_payment:

        raise HTTPException(
            status_code = 400, 
            detail = "Payment already exists"
        )
    

    new_payment = Payment(
        order_id = order.id, 
        amount = order.total_amount, 
        status = "SUCCESS"
    )

    db.add(new_payment)

    db.commit()

    db.refresh(new_payment)

    return new_payment 


@router.put("/{order_id}/status")
def update_order_status(
    order_id : int , 
    order_status : OrderStatusUpdate, 
    current_user = Depends(get_current_user), 
    db : Session = Depends(get_db)
):
    if current_user.role != "Admin":

        raise HTTPException(
            status_code = 403, 
            detail = "Access Denied"
        )
    
    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:

        raise HTTPException(
            status_code = 404, 
            detail = "Order Not Found"
        )
    
    order.status = order_status.status

    db.commit()

    db.refresh(order)

    return order



    