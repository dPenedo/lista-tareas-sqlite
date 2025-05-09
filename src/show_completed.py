import sqlite3
from .show_tasks import show_tasks
from src.ui.colorize import colorize, Color


def show_completed(conn: sqlite3.Connection):
    print(f"Here are the tasks that have been {colorize("completed", Color.BOLD)}")
    show_tasks(conn, "completed")
