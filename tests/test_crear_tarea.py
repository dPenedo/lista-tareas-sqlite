from src.crear_tarea import crear_tarea
from src.inicializar_base_de_datos import inicializar_base_de_datos
import os
import sqlite3
from unittest.mock import patch
from main import BASE_DE_DATOS


base_de_datos = BASE_DE_DATOS


def setup_module():
    # Inicializa la base de datos antes de ejecutar las pruebas
    inicializar_base_de_datos(base_de_datos)
    insertar_tarea_prueba()


def insertar_tarea_prueba():
    conn = sqlite3.connect(base_de_datos)
    cursor = conn.cursor()
    # Inserta una tarea específica en la base de datos
    cursor.execute(
        "INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?, ?, ?)",
        ("Tarea de prueba", "Descripción de la tarea de prueba", "2025-01-01"),
    )
    conn.commit()
    conn.close()


# TODO: para poder probar la funcion de crear tareas hay que refactorizar de tal forma que la funcion que cree la tarea no contenga los inputs, hay que ponerlos externos
# def test_crear_tarea():
#     conn = sqlite3.connect(base_de_datos)
#     cursor = conn.cursor()
#     assert crear_tarea(conn) is True
#     cursor.close()
#     conn.close()
#
# def test_estructura_tarea():
#     conn = sqlite3.connect(base_de_datos)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM tareas WHERE nombre = 'Tarea de prueba';")
#     tarea = cursor.fetchone()
#     assert tarea[1] == "Tarea de prueba"
#     assert tarea[2] == "Descripción de la tarea de prueba"
#     assert tarea[4] == "2025-01-01"
#     cursor.close()
#     conn.close()
