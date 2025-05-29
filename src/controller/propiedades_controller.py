import psycopg2
import sys
import os
sys.path.append(".")
from config.secret_config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD
from src.model.inverse_mortage import Property

def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require')
    return conn

def get_cursor():
    cursor = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)
    return cursor

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

def insert_property(property: Property):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open('src/sql/insert_property.sql', 'r') as query:
            query = query.read()
        cursor.execute(query, property.to_tuple())
        conn.commit()
        print("Propiedad insertada correctamente.")
    except Exception as e:
        print(f"Error inserting property: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_property(id: str):
    
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

def buscar_propiedades_por_nombre(nombre: str):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open('src/sql/select_properties_by_name.sql', 'r') as file:
            query = file.read()
        cursor.execute(query, (f"%{nombre}%",))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error buscando propiedades por nombre: {e}")
        return []
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

def drop_table_property():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open('src/sql/drop_table_property.sql', 'r') as query:
            query = query.read()
        cursor.execute(query)
        conn.commit()
        print("Tabla propiedad eliminada correctamente.")
    except Exception as e:
        print(f"Error eliminando la tabla propiedad: {e}")
    finally:
        cursor.close()
        conn.close()

def reset_table_property():
    drop_table_property()
    create_table_property()

create_table_property()
# propiedad_ejemplo = Property(3, 800000000, 18, True, True)
# insert_property(propiedad_ejemplo)
#new_property = Property(5, 600000000, 18, True, True)
# update_property(6, new_property)
# select_property_properties(6)
# delete_person(1)
# delete_property(3)


