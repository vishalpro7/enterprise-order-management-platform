from database.db import engine
from database.db import Base
from models.payment_model import Payment
from models.user_model import User
from routers.products import Product
from models.order_model import Order
from models.order_item_model import OrderItem


Base.metadata.create_all(bind = engine)

