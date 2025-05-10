import psycopg2
import sys
sys.path.append("c:/Users/emanu/Desktop/inverse_mortage")  # Agrega el directorio raíz al path
from secret_config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD
from decimal import Decimal
import os
sys.path.append("src")

from model.inverse_mortage import Property

# PGHOST = os.getenv("PGHOST")
# PGDATABASE = os.getenv("PGDATABASE")
# PGUSER = os.getenv("PGUSER")
# PGPASSWORD = os.getenv("PGPASSWORD")


def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require')
    return conn


def insert_propiedad(propiedad: Property):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/insert_property.sql', 'r') as consulta:
            consulta = consulta.read()
            
        tuple_propiedad = (
            propiedad.stratum,
            propiedad.commercial_value,
            propiedad.antiqueness,
            propiedad.legality,
            propiedad.taxes_ok
        )
        cursor.execute(consulta, tuple_propiedad)
            
        conn.commit()
        print("Propiedad insertada correctamente.")
    except Exception as e:
        print(f"Error inserting propiedad: {e}")
    finally:
        cursor.close()
        conn.close()

# Asegúrate de que la clase Property esté bien definida en model.inverse_mortage
propiedad_Prueba = Property(3, Decimal("200000000"), 8, True, True)
insert_propiedad(propiedad_Prueba)
