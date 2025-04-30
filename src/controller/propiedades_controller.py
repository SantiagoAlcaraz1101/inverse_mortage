import psycopg2
import sys 
from dotenv import load_dotenv
import os
sys.path.append("src")

from model.inverse_mortage import Property
load_dotenv()



PGHOST= os.getenv("PGHOST")
PGDATABASE= os.getenv("PGDATABASE")
PGUSER= os.getenv("PGUSER")
PGPASSWORD= os.getenv("PGPASSWORD")


def main_cursor():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)
    cursor = conn.cursor()
    return cursor

def insert_propiedad(propiedad: Property):
    cursor = main_cursor()
    try:
        insertar = f"INSERT INTO 'Propiedad' (estrato, valor_comercial, antiguedad, legalidad, impuestos) VALUES ({propiedad.stratum}, {propiedad.commercial_value}, {propiedad.antiqueness}, {propiedad.legality}, {propiedad.taxes_ok})"
        cursor.execute(insertar)
        cursor.connection.commit()
    except Exception as e:
        print(f"Error inserting propiedad: {e}")
    finally:
        cursor.close()
        cursor.connection.close()



propiedad_Prueba = Property(3, 700e6, 8, True, True)

insert_propiedad(propiedad_Prueba)        


