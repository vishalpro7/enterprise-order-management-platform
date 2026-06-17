from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus

password = quote_plus("Basuvi@200607")

DATABASE_URL = (
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/EnterpriseOrderDB"
)
print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    echo = True
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()

