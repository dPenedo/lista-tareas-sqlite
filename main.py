from pathlib import Path
import sqlite3
from src import (
    show_pending,
    show_descriptions,
    mark_as_completed,
    show_completed,
    edit_task,
    start_database,
    delete_task,
    create_task,
    get_data,
)
from src.ui.colorize import colorize

import os

DATABASE = "db/lista_de_tareas.db"


def mostrar_menu():
    print(f"{colorize("1. ", "BLUE")} Create a new task")
    print(f"{colorize("2. ", "BLUE")} Mark a task as completed")
    print(f"{colorize("3. ", "BLUE")} Edit a pending task")
    print(f"{colorize("4. ", "BLUE")} Show descriptions of pending tasks")
    print(f"{colorize("5. ", "BLUE")} Show completed tasks")
    print(f"{colorize("6. ", "BLUE")} Show pending tasks for this week")
    print(f"{colorize("7. ", "BLUE")} Delete a pending task")
    print(f"{colorize("8. ", "BLUE")} TEST")
    print(f"{colorize("0. ", "BLUE")} Exit")


def main():

    Path("db").mkdir(exist_ok=True)
    _ = start_database.start_database(DATABASE)
    conn = sqlite3.connect(DATABASE)
    _ = os.system("clear")
    print(f"\n{colorize("Hello! 👋 Welcome to your Task Manager" ,"BLUE")}")
    content_to_show = "simple"
    while True:
        print("\nHere are your pending tasks:\n")
        if content_to_show == "simple":
            _ = show_pending.show_pending(conn)
        elif content_to_show == "descripcion":
            _ = show_descriptions.show_descriptions(conn)
            content_to_show = "simple"
        print("\n╚" + "═" * 48 + "╝")
        print("╔" + "═" * 48 + "╗")
        print(colorize("What would you like to do?", "BLUE"))
        mostrar_menu()
        opcion = input()
        if opcion == "1":
            print("Great, let's create a new task")
            print(
                "The following values are required: \n- Name \n- Task description\n- Task deadline"
            )
            print(colorize("***************************", "RESET"))
            name, descripcion, date_deadline = get_data.get_new_task()
            create_task.create_task(conn, name, descripcion, date_deadline)

            _ = os.system("clear")
            print("Task Created!")
        elif opcion == "2":
            selection = get_data.get_selected_task(conn)
            mark_as_completed.mark_as_completed(conn, selection)
            _ = os.system("clear")
        elif opcion == "3":
            _ = os.system("clear")
            edit_task.edit_task(conn)
        elif opcion == "4":
            _ = os.system("clear")
            content_to_show = "description"
            print("Now showing descriptions of the tasks")
        elif opcion == "5":
            _ = os.system("clear")
            show_completed.show_completed(conn)
        elif opcion == "6":
            _ = os.system("clear")
            print("Pending tasks for this week is a feature to be implemented")
        elif opcion == "7":
            _ = os.system("clear")
            delete_task.delete_task(conn)
        elif opcion == "8":
            _ = os.system("clear")
            get_data.get_selected_task(conn)
        elif opcion == "0":
            print("🏃 See you soon!")
            break
        else:
            print("Invalid option. Please select a valid option.")
    conn.close()


if __name__ == "__main__":
    main()
