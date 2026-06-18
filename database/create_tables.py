from database.db import engine
from database.db import Base

from models.user_model import User
from routers.products import Product

Base.metadata.create_all(bind = engine)

