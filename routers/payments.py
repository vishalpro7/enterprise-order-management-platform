from fastapi import APIRouter

router = APIRouter(
    prefix = "/payments",
    tags = ["Payments"]
)

@router.post("/")
def create_payment():

    return {
        "message" : "Payment Route Working"
    }