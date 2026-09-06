from sqlalchemy.orm import Session
from models.order_status_history_model import OrderStatusHistory

def create_status_history(
        db : Session, 
        order_id : int, 
        old_status : str, 
        new_status : str, 
        changed_by : int
):
    history = OrderStatusHistory(
        order_id = order_id, 
        old_status = old_status, 
        new_status = new_status, 
        changed_by = changed_by
    )

    db.add(history)

    return history