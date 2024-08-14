from sqlalchemy import create_engine, text, URL
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqldb://jai:admin123@localhost/common_contributions_tracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

