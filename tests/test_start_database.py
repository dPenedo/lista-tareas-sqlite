import os
import sqlite3
from src.start_database import start_database
from main import DATABASE


database = DATABASE

def test_inicializar_base_de_datos():
    # Cleanup: Ensure the database doesn't exist before the test
    if os.path.exists(database):
        os.remove(database)

    conn = start_database(database)
    assert conn is not None

    # Ensure the database is closed after testing
    conn.close()

def test_estructura_base_de_datos():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columns = cursor.fetchall()

    assert len(columns) == 5
    assert columns[0][1] == "id"
    assert columns[1][1] == "nombre"
    assert columns[2][1] == "descripcion"
    assert columns[3][1] == "completada"
    assert columns[4][1] == "fecha_limite"
    
    cursor.close()
    conn.close()

def test_tipos_de_datos():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columnas = cursor.fetchall()

    assert columnas[0][2] == "INTEGER"
    assert columnas[1][2] == "TEXT"
    assert columnas[2][2] == "TEXT"
    assert columnas[3][2] == "INTEGER"
    assert columnas[4][2] == "DATE"

    cursor.close()
    conn.close()
database = "db/lista_de_tareas.db"


def test_inicializar_base_de_datos():
    conn = start_database(database)
    assert conn is not None


def test_estructura_base_de_datos():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columns = cursor.fetchall()

    assert len(columns) == 5
    assert columns[0][1] == "id"
    assert columns[1][1] == "nombre"
    assert columns[2][1] == "descripcion"
    assert columns[3][1] == "completada"
    assert columns[4][1] == "fecha_limite"
    cursor.close()


def test_tipos_de_datos():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columnas = cursor.fetchall()

    assert columnas[0][2] == "INTEGER"
    assert columnas[1][2] == "TEXT"
    assert columnas[2][2] == "TEXT"
    assert columnas[3][2] == "INTEGER"
    assert columnas[4][2] == "DATE"

    cursor.close()
