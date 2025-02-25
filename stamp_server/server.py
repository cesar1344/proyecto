import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

passw = os.environ.get("PASS")
print(passw)