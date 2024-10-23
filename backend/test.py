from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://username:password@localhost:5432/dbname")

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")
    