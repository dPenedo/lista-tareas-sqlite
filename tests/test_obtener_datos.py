from src.obtener_datos import obtener_tarea_nueva, obtener_tarea_seleccionada, obtener_fecha
from unittest.mock import patch

mock_input_values = ["Nombre de prueba", "Descripcion de prueba", "2/3/2024"]

def mock_input(prompt):
    return mock_input_values.pop(0)

@patch("builtins.input", side_effect=mock_input)
def test_obtener_tarea_nueva(mock_input):
    nombre, descripcion, fecha_limite = obtener_tarea_nueva()

    assert nombre == "Nombre de prueba"
    assert descripcion == "Descripcion de prueba"
    assert fecha_limite == "2/3/2024"

