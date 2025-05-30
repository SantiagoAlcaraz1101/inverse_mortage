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


def delete_property(propiedad_id):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM propiedades WHERE id = ?", (propiedad_id,))
        connection.commit()
    finally:
        connection.close()


def update_property(propiedad_id, estrato, valor_comercial, antiguedad, legalidad, titulo_propiedad):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            UPDATE propiedades 
            SET estrato = ?, valor_comercial = ?, antiguedad = ?, legalidad = ?, titulo_propiedad = ?
            WHERE id_propiedad = ?
        """, (estrato, valor_comercial, antiguedad, legalidad, titulo_propiedad, propiedad_id))
        connection.commit()
    finally:
        connection.close()


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

        

def select_property_properties(propiedad_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT estrato, valor_comercial, antiguedad, legalidad, titulo_propiedad, id_propiedad FROM propiedades WHERE id = ?", (propiedad_id,))
    propiedad = cursor.fetchone()
    connection.close()
    return propiedad

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


