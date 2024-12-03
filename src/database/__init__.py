from src.database.database import Base, engine
from src.database.account import AccountTable

Base.metadata.create_all(bind=engine)
