import psycopg2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config.secret_config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD
from src.model.inverse_mortage import Property

def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require')
    return conn

def create_table_property():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/create_table_property.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query)
            
        conn.commit()
        print("Tabla propiedad creada correctamente.")

    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_property(propiedad: Property):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/insert_property.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, propiedad.to_tuple())
            
        conn.commit()
        print("Propiedad insertada correctamente.")
    except Exception as e:
        print(f"Error inserting propiedad: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_property(id: int):
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/delete_property.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, (id,))
            
        conn.commit()
        print("Propiedad eliminada correctamente.")
    except Exception as e:
        print(f"Error deleting propiedad: {e}")
    finally:
        cursor.close()
        conn.close()

def update_property(id: int, property: Property):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/update_property.sql', 'r') as query:
            query = query.read()
            
        new_property = property.to_tuple()
        cursor.execute(query, (*new_property, id))
            
        conn.commit()
        print("Propiedad actualizada correctamente.")
    except Exception as e:
        print(f"Error updating propiedad: {e}")
    finally:
        cursor.close()
        conn.close()


def select_property_properties(id_property: int):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/select_property.sql', 'r') as query:
            query = query.read()
        cursor.execute(query, (id_property,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error selecting all properties: {e}")
    finally:
        cursor.close()
        conn.close()

#Ejemplo de uso

create_table_property()
propiedad_ejemplo = Property(3, 800000000, 18, True, True)
insert_property(propiedad_ejemplo)
#new_property = Property(5, 600000000, 18, True, True)
# update_property(6, new_property)
# select_property_properties(6)
# delete_person(1)
# delete_property(3)

