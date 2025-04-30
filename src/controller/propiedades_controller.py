import psycopg2
import sys 
from dotenv import load_dotenv
import os
sys.path.append("src")

from model.inverse_mortage import Property
load_dotenv()



#PGHOST= os.getenv("PGHOST")
#PGDATABASE= os.getenv("PGDATABASE")
#PGUSER= os.getenv("PGUSER")
#PGPASSWORD= os.getenv("PGPASSWORD")

PGHOST='ep-bitter-scene-a48mvj5y-pooler.us-east-1.aws.neon.tech'

PGDATABASE='neondb'

PGUSER='neondb_owner'

PGPASSWORD='npg_NGKnv35XzCmU'

#def cursor():
#    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)
#    cursor = conn.cursor()
#    return cursor

def insert_propiedad(propiedad: Property):
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO propiedadas (estrato, valor_comercial, antiguedad, legalidad, impuestos) VALUES (%s, %s, %s, %s, %s)",
                       (propiedad.stratum, propiedad.commercial_value, propiedad.antiqueness, propiedad.legality, propiedad.taxes_ok))
        cursor.connection.commit()
    except Exception as e:
        print(f"Error inserting propiedad: {e}")
    finally:
        cursor.close()
        cursor.connection.close()



propiedad_Prueba = Property(3, 700e6, 8, True, True)

insert_propiedad(propiedad_Prueba)        


