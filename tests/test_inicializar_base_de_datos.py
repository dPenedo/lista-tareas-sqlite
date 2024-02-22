from src.inicializar_base_de_datos import inicializar_base_de_datos
import os
import sqlite3

base_de_datos = "db/lista_de_tareas.db"


def test_inicializar_base_de_datos():
    conn = inicializar_base_de_datos(base_de_datos)
    assert conn is not None

def test_estructura_base_de_datos():
    conn = sqlite3.connect(base_de_datos)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columnas = cursor.fetchall()

    assert len(columnas) == 5
    assert columnas[0][1] == "id"
    assert columnas[1][1] == "nombre"
    assert columnas[2][1] == "descripcion"
    assert columnas[3][1] == "completada"
    assert columnas[4][1] == "fecha_limite"
    cursor.close()

def test_tipos_de_datos():
    conn = sqlite3.connect(base_de_datos)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info('tareas');")
    columnas = cursor.fetchall()

    assert columnas[0][2] == "INTEGER"
    assert columnas[1][2] == "TEXT"
    assert columnas[2][2] == "TEXT"
    assert columnas[3][2] == "INTEGER"
    assert columnas[4][2] == "DATE"

    cursor.close()


