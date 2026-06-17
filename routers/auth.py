from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal
from models.user_model import User
from schemas.user_schema import UserCreate
from schemas.user_schema import UserResponse 

