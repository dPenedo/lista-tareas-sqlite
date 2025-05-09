import sqlite3

from src.ui.colorize import Color, colorize


COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"


def show_descriptions(conn: sqlite3.Connection):
    print("Here are the pending tasks along with their descriptions:")
    cursor = conn.cursor()
    _ = cursor.execute(
        "SELECT id, nombre, descripcion FROM tareas WHERE completada = 0"
    )
    pending_tasks = cursor.fetchall()
    print(colorize("Descriptions", Color.BLUETITLE))
    for task in pending_tasks:
        print(
            f"{COLOR_BLUE}{colorize(str(task[0]), Color.BLUE)}. {str(task[1])}.{colorize(str(task[2]), Color.BOLD)}"
        )

