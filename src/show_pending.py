import sqlite3
from typing import List, Tuple
from src.ui import colorize


COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"

COLOR_UNDERLINE = "\033[4m"  # Subrayado


def show_pending(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM tareas WHERE completada = 0")
    # WARN: deprecated
    pending_tasks: List[Tuple[int, str]] = cursor.fetchall()

    print(colorize("Pending tasks: ", "BLUE_TITLE"))
    for task_id, task_name in pending_tasks:
        print(f"{colorize(str(task_id), "BLUE")} {task_name}")
