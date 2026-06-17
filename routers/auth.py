from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from auth.security import hash_password

from database.db import SessionLocal
from models.user_model import User
from schemas.user_schema import UserCreate
from schemas.user_schema import UserResponse
from schemas.user_schema import (UserLogin, TokenResponse)
from auth.security import (verify_password, create_access_token) 

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
        password = hash_password(user.password),
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

@router.get("/users/{user_id}", response_model = UserResponse)
def get_user(
    user_id : int, db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user: 
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found!"
        )

    return user

@router.post(
    "/login",
    response_model = TokenResponse
)
def login_user(login_data : UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Credentials!!"
        )
    
    if not verify_password(
        login_data.password,
        user.password
    ):
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Password!"
        )
    
    token = create_access_token(
        {
            "sub" : user.email
        }
    )

    return {
        "access_token" : token,
        "token_type" : "bearer"
    }



