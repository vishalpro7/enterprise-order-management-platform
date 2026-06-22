from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):

    product_id : int
    quantity : int


class OrderCreate(BaseModel):

    items : List[OrderItemCreate]


class OrderResponse(BaseModel):

    id : int
    user_id : int
    total_amount : int

    class Config :
        from_attributes = True


class OrderSummary(BaseModel):

    id : int
    user_id : int
    total_amount : int

    class Config:
        from_attributes = True


class OrderItemResponse(BaseModel):

    product_id : int
    quantity : int

    class Config:
        from_attributes = True

class OrderDetailResponse(BaseModel):

    id : int
    user_id : int
    total_amount : int
    order_items : List[OrderItemResponse]

    class Config:
        from_attributes = True 