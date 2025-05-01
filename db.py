from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host"),
    port=int(os.getenv("port")),
    database=os.getenv("dbname")
)

engine = create_engine(url)
