import os

COLOR_RESET = "\033[0m"  # Reset color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Bold
COLOR_BLUE_TITLE = "\033[34;1;4m"  # Blue, bold, underlined


def delete_task(conn):
    # TODO: Externalize getting task ID selection into a separate function: get_selected_task
    print(f"{COLOR_BOLD}Which task would you like to delete?{COLOR_RESET}\n")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nombre, descripcion, fecha_limite FROM tareas WHERE completada = 0"
    )
    pending_tasks = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Tasks available for deletion:{COLOR_RESET}")
    for task in pending_tasks:
        print(
            f"{COLOR_BLUE}{task[0]}{COLOR_RESET}. {task[1]}.{COLOR_BOLD} {task[2]}{COLOR_RESET} ({task[3]})"
        )
    chosen_task = int(input("Select a task number: "))

    found_task = None

    for task in pending_tasks:
        if task[0] == chosen_task:
            found_task = task
            break

    if found_task:
        print(f"The selected task is:{COLOR_BOLD}{found_task[1]}{COLOR_RESET}")
        print(f"{COLOR_BOLD}  Are you sure you want to delete it?{COLOR_RESET}")
        confirm = input(
            'Press "s" to confirm deletion or any other key to return to the main menu\n'
        )
        if confirm.lower() == "s":
            cursor.execute("DELETE FROM tareas WHERE id = ?;", (found_task[0],))
            os.system("clear")
            print(f"The task {found_task[1]} has been deleted.")
        else:
            os.system("clear")
            print("Returning to the main menu.")

    else:
        print("Task not found.")
