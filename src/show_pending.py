import sqlite3
from .show_tasks import show_tasks
from src.ui.colorize import Color, colorize


def show_pending(conn: sqlite3.Connection):
    print(colorize("Pending tasks: ", Color.BLUETITLE))
    show_tasks(conn, "pending")
