import psycopg2
import sys
from dotenv import load_dotenv
from decimal import Decimal
import os
sys.path.append("src")

from model.inverse_mortage import Property
load_dotenv()


PGHOST = os.getenv("PGHOST")
PGDATABASE = os.getenv("PGDATABASE")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")


def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require', options="endpoint=ep-bitter-scene-a48mvj5y")
    return conn


def insert_propiedad(propiedad: Property):
    conn = connect_db()
    cursor = conn.cursor()
    try:

        cursor.execute(
            """
            INSERT INTO "Propiedad" (estrato, valor_comercial, antiguedad, legalidad, impuestos)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                propiedad.stratum,
                propiedad.commercial_value,
                propiedad.antiqueness,
                propiedad.legality,
                propiedad.taxes_ok
            )
        )
        conn.commit()
        print("Propiedad insertada correctamente.")
    except Exception as e:
        print(f"Error inserting propiedad: {e}")
    finally:
        cursor.close()
        conn.close()

# Asegúrate de que la clase Property esté bien definida en model.inverse_mortage
propiedad_Prueba = Property(3, Decimal("100000000"), 8, True, True)
insert_propiedad(propiedad_Prueba)
