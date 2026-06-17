from jose import jwt
from jose import JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import SessionLocal
from models.user_model import User


SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl = "/auth/login"
    )


def verify_token(token : str):
    
    try :
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            return None
        
        return email
    
    except JWTError:
        return None

def get_db():

    db = SessionLocal()

    try: 
        yield db

    finally:
        db.close()


def get_current_user(
        token : str = Depends(oauth2_scheme),
        db : Session = Depends(get_db)
):
    email = verify_token(token)

    if email is None:
        raise HTTPException(
            status_code = 401,
            details = "Invalid Token!"
        )
    
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code = 401,
            details = "User Not Found!"
        )
    
    return user