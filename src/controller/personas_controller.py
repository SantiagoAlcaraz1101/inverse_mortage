import psycopg2
import sys 
from dotenv import load_dotenv
import os
sys.path.append("src")

from model.inverse_mortage import Person
load_dotenv()



PGHOST= os.getenv("PGHOST")
PGDATABASE= os.getenv("PGDATABASE")
PGUSER= os.getenv("PGUSER")
PGPASSWORD= os.getenv("PGPASSWORD")






