from src.obtener_datos import (
    obtener_tarea_nueva,
    obtener_tarea_seleccionada,
    obtener_fecha,
)
from unittest.mock import patch
from datetime import date
import sqlite3

mock_input_values_tarea_nueva = [
    "Nombre de prueba",
    "Descripcion de prueba",
    "2",
    "3",
    "2024",
]


def mock_input_tarea_nueva(prompt):
    return mock_input_values_tarea_nueva.pop(0)


@patch("builtins.input", side_effect=mock_input_tarea_nueva)
def test_obtener_tarea_nueva(mock_input):
    nombre, descripcion, fecha_limite = obtener_tarea_nueva()
    assert nombre == "Nombre de prueba"
    assert descripcion == "Descripcion de prueba"
    assert fecha_limite == date(2024, 3, 2)


# Funciona!  Habria que sumarle alguna tarea más de prueba para ver
mock_input_values_tarea_seleccionada = ["2"]


def mock_input_tarea_seleccionada(prompt):
    return mock_input_values_tarea_seleccionada.pop(0)


@patch("builtins.input", side_effect=mock_input_tarea_seleccionada)
def test_tarea_seleccionada(mock_input):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        completada INTEGER DEFAULT 0,
        fecha_limite DATE
    )"""
    )
    tareas_de_test = [
        ("Tarea 1", "Descripción de la tarea 1", "2024-02-22"),
        ("Tarea 2", "Descripción de la tarea 2", "2024-02-23"),
        ("Tarea 3", "Descripción de la tarea 3", "2024-02-24"),
        ("Tarea 4", "Descripción de la tarea 4", "2024-02-25"),
    ]
    cursor.executemany(
        "INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?, ?, ?)",
        tareas_de_test,
    )
    conn.commit()
    tarea_seleccionada = obtener_tarea_seleccionada(conn)
    assert tarea_seleccionada[0] == 2


mock_input_values_fecha = ["4", "4", "2024"]


def mock_input_fecha(prompt):
    return mock_input_values_fecha.pop(0)


@patch("builtins.input", side_effect=mock_input_fecha)
def test_obtener_fecha(mock_input):
    fecha_limite = obtener_fecha()
    assert fecha_limite == date(2024, 4, 4)
