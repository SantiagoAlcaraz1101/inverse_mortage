import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import psycopg2
from config.secret_config import PGHOST, PGDATABASE, PGUSER, PGPASSWORD

from src.model.inverse_mortage import Person, Property

def connect_db():
    conn = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD, sslmode='require')
    return conn

def get_cursor():
    cursor = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)
    return cursor

def create_table_people():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/create_table_personas.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query)
            
        conn.commit()
        print("Tabla personas creada correctamente.")

    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_person(person: Person):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/insert_persona.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, person.to_tuple())
            
        conn.commit()
        print("Persona insertada correctamente.")
    except Exception as e:
        print(f"Error inserting persona: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_person(id_person: int):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/delete_person.sql', 'r') as query:
            query = query.read()
            
        cursor.execute(query, (id_person,))
            
        conn.commit()
        print("Persona eliminada correctamente.")
    except Exception as e:
        print(f"Error deleting persona: {e}")
    finally:
        cursor.close()
        conn.close()

def update_persona(id_person: int, person: Person):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/update_person.sql', 'r') as query:
            query = query.read()
            
        new_person = person.to_tuple()
        cursor.execute(query, (*new_person, id_person))
            
        conn.commit()
        print("Persona actualizada correctamente.")
    except Exception as e:
        print(f"Error updating persona: {e}")
    finally:
        cursor.close()
        conn.close()

def select_person_properties(id_person: int):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        with open ('src/sql/select_person.sql', 'r') as query:
            query = query.read()
        cursor.execute(query, (id_person,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error selecting all properties: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_personas_por_nombre(nombre: str):
    conn = connect_db() 
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM personas WHERE nombre ILIKE %s;"
        cursor.execute(query, (f"%{nombre}%",))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error buscando personas por nombre: {e}")
        return []
    finally:
        cursor.close()
        conn.close()



def drop_and_recreate_table_people():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS personas CASCADE;")
        conn.commit()
        print("Tabla personas eliminada correctamente.")
        create_table_people()
    except Exception as e:
        print(f"Error dropping and recreating table: {e}")
    finally:
        cursor.close()
        conn.close()
# Ejemplo de uso
create_table_people()
#persona_ejemplo = Person("James", 70, False, False, True, Property(3, 800000000, 18, True, True))
# insert_person(persona_ejemplo)
# new_person = Person("Emanuel", 70, False, False, True, 6)






