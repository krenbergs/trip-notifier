from src.settings import settings
from src.database.database import Base, engine


def reset_database():
    if settings.postgres_db == "development-database":
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

reset_database()