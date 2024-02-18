from src.obtener_datos import obtener_tarea_nueva, obtener_tarea_seleccionada, obtener_fecha
from unittest.mock import patch
from datetime import date

mock_input_values_tarea_nueva = ["Nombre de prueba", "Descripcion de prueba", "2", "3", "2024"]

def mock_input_tarea_nueva(prompt):
    return mock_input_values_tarea_nueva.pop(0)

@patch("builtins.input", side_effect=mock_input_tarea_nueva)
def test_obtener_tarea_nueva(mock_input):
    nombre, descripcion, fecha_limite = obtener_tarea_nueva()
    assert nombre == "Nombre de prueba"
    assert descripcion == "Descripcion de prueba"
    assert fecha_limite == date(2024, 3, 2)





mock_input_values_fecha = ["4", "4", "2024"]

def mock_input_fecha(prompt):
    return mock_input_values_fecha.pop(0)

@patch("builtins.input", side_effect=mock_input_fecha)
def test_obtener_fecha(mock_input):
    fecha_limite = obtener_fecha()
    assert fecha_limite == date(2024, 4, 4)
