from fastapi import APIRouter

router = APIRouter(
    prefix = "/orders",
    tags = ["Orders"]
)

@router.get("/")
def test_orders():
    return {"message": "Orders Working"}