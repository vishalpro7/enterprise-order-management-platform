from pydantic import BaseModel

class PaymentCreate(BaseModel):

    order_id : int


class PaymentResponse(BaseModel):

    id : int
    
    order_id : int

    amount : int

    status : str


    class Config:

        from_attributes = True