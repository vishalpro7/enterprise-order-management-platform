from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "mssql+pyodbc://@"
    "(localdb)\\MSSQLLocalDB/"
    "EnterpriseOrderDB?"
    "driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
)

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

