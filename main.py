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

import os


# Colors
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"
COLOR_WHITE = "\033[37m"
COLOR_BOLD = "\033[1m"  # Bold
COLOR_RESET = "\033[0m"  # Reset color

DATABASE = "db/lista_de_tareas.db"


def mostrar_menu():
    print(f"{COLOR_BLUE}1.{COLOR_RESET} Create a new task")
    print(f"{COLOR_BLUE}2.{COLOR_RESET} Mark a task as completed")
    print(f"{COLOR_BLUE}3.{COLOR_RESET} Edit a pending task")
    print(f"{COLOR_BLUE}4.{COLOR_RESET} Show descriptions of pending tasks")
    print(f"{COLOR_BLUE}5.{COLOR_RESET} Show completed tasks")
    print(f"{COLOR_BLUE}6.{COLOR_RESET} Show pending tasks for this week")
    print(f"{COLOR_BLUE}7.{COLOR_RESET} Delete a pending task")
    print(f"{COLOR_BLUE}8.{COLOR_RESET} TEST")
    print(f"{COLOR_BLUE}0.{COLOR_RESET} Exit")


def main():
    start_database.start_database(DATABASE)
    conn = sqlite3.connect(DATABASE)
    os.system("clear")
    print(f"\n{COLOR_BLUE}Hello! 👋 Welcome to your Task Manager{COLOR_RESET}")
    content_to_show = "simple"
    while True:
        print("\nHere are your pending tasks:\n")
        if content_to_show == "simple":
            show_pending.show_pending(conn)
        elif content_to_show == "descripcion":
            show_descriptions.show_descriptions(conn)
            content_to_show = "simple"
        print("\n╚" + "═" * 48 + "╝")
        print("╔" + "═" * 48 + "╗")
        print(f"\n{COLOR_BLUE_TITLE}What would you like to do?{COLOR_RESET}")
        mostrar_menu()
        opcion = input()
        if opcion == "1":
            print("Great, let's create a new task")
            print(
                "The following values are required: \n- Name \n- Task description\n- Task deadline"
            )
            print(f"\n{COLOR_BOLD}***************************{COLOR_RESET}\n")
            name, descripcion, date_deadline = get_data.get_new_task()
            create_task.create_task(conn, name, descripcion, date_deadline)

            os.system("clear")
            print("Task Created!")
        elif opcion == "2":
            selection = get_data.get_selected_task(conn)
            mark_as_completed.mark_as_completed(conn, selection)
            os.system("clear")
        elif opcion == "3":
            os.system("clear")
            edit_task.edit_task(conn)
        elif opcion == "4":
            os.system("clear")
            content_to_show = "description"
            print("Now showing descriptions of the tasks")
        elif opcion == "5":
            os.system("clear")
            show_completed.show_completed(conn)
        elif opcion == "6":
            os.system("clear")
            print("Pending tasks for this week is a feature to be implemented")
        elif opcion == "7":
            os.system("clear")
            delete_task.delete_task(conn)
        elif opcion == "8":
            os.system("clear")
            get_data.get_selected_task(conn)
        elif opcion == "0":
            print("🏃 See you soon!")
            break
        else:
            print("Invalid option. Please select a valid option.")
    conn.close()


if __name__ == "__main__":
    main()
