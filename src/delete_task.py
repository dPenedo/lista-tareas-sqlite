import os
import sqlite3
from .ui.colorize import Color, colorize
from .get_data import get_selected_task


def delete_task(conn: sqlite3.Connection):
    print(colorize("Which task would you like to delete?", Color.BOLD))
    task_to_delete = get_selected_task(conn)
    if task_to_delete:
        print(colorize("  Are you sure you want to delete it?", Color.RED))
        confirm = input(
            'Press "y" to confirm deletion or any other key to return to the main menu\n'
        )
        if confirm.lower() == "y":
            cursor = conn.cursor()
            _ = cursor.execute("DELETE FROM tareas WHERE id = ?;", (task_to_delete,))
            _ = os.system("clear")
            print(f"The task {task_to_delete} has been deleted.")
        else:
            _ = os.system("clear")
            print("Returning to the main menu.")
