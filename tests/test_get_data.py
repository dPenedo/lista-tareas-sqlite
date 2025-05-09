from src.get_data import (
    get_selected_task,
)
from unittest.mock import patch
from datetime import date
import sqlite3


# Test para seleccionar una tarea
@patch("builtins.input", side_effect=["2"])
def test_tarea_seleccionada(mock_input):
    """
    Verifica que get_selected_task pueda seleccionar correctamente una tarea
    de la base de datos en memoria.
    """
    conn = sqlite3.connect(":memory:")
    try:
        cursor = conn.cursor()
        _ = cursor.execute(
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
        _ = cursor.executemany(
            "INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?, ?, ?)",
            tareas_de_test,
        )
        conn.commit()

        tarea_seleccionada = get_selected_task(conn)
        assert tarea_seleccionada == 2  # ID de la tarea seleccionada
    finally:
        conn.close()
