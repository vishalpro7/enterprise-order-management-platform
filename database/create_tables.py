from database.db import engine
from database.db import Base

from models.user_model import User

Base.metadata.create_all(bind = engine)

