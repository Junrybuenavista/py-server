import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:1234@localhost:5432/postgres")

    # Other configuration settings
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

# Check if DATABASE_URL is being set
if __name__ == "__main__":
    print(f"Database URL: {Config.DATABASE_URL}")  # Add this line to debug
    print(f"Debug Mode: {Config.DEBUG}")
    print(f"Secret Key: {Config.SECRET_KEY}")
