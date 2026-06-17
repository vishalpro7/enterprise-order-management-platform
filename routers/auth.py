from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import SessionLocal
from models.user_model import User
from schemas.user_schema import UserCreate
from schemas.user_schema import UserResponse 

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()


@router.post("/register", response_model = UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name = user.name,
        email = user.email,
        password = user.password,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get(
    "/users",
    response_model=List[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()

    return users