import sqlite3

from src.ui.colorize import colorize, Color


def show_tasks(conn: sqlite3.Connection, condition: str):
    cursor = conn.cursor()
    condition_to_print = ""
    if condition == "pending":
        condition_to_print = "WHERE completada = 0"
    if condition == "completed":
        condition_to_print = "WHERE completada = 1"
    _ = cursor.execute(f"SELECT id, nombre FROM tareas {condition_to_print}")
    pending_tasks: list[tuple[int, str]] = cursor.fetchall()

    for task_id, task_name in pending_tasks:
        print(f"{colorize(str(task_id), Color.BLUE)} {task_name}")
