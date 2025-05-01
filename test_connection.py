from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env
load_dotenv(dotenv_path="./.env")

# Locate the actual .env file Python is using
env_path = find_dotenv()
print("🔍 Loading .env from:", env_path)


# Print environment variables to verify correct values are loaded
print("ENV VALUES LOADED:")
print("user:", os.getenv("user"))
print("host:", os.getenv("host"))
print("port:", os.getenv("port"))
print("dbname:", os.getenv("dbname"))

# Build connection URL safely to handle special characters in password
url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host"),
    port=int(os.getenv("port")),
    database=os.getenv("dbname")
)

# Create engine and test the connection
try:
    engine = create_engine(url)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("✅ Connected! Current time on server:", result.scalar())
except Exception as e:
    print("❌ Connection failed:", e)
