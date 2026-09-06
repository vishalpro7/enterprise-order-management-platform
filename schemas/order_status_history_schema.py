from pydantic import BaseModel
from datetime import datetime

class OrderStatusHistoryResponse(BaseModel):
    id : int
    order_id : int
    old_status : str
    new_status : str
    changed_by : int
    changed_at : datetime

class Config:
    from_attributes = True