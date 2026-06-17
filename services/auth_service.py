from jose import jwt
from datetime import datetime, timedelta




SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_token(token : str):
    pass