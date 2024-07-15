from sqlalchemy import create_engine, text
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



# Check Database Connection
# def check_db_connection():
#     try:
#         # Create a session and execute a simple query
#         with SessionLocal() as session:
#             result = session.execute(text("SELECT 1")).scalar()
#         print("Database connection successful!")
#         print(result)
#     except Exception as e:
#         print(f"Database connection failed: {e}")
#         return None
