COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"


def show_descriptions(conn):
    print("Here are the pending tasks along with their descriptions:")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion FROM tareas WHERE completada = 0")
    pending_tasks = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Descriptions:{COLOR_RESET}")
    for task in pending_tasks:
        print(
            f"{COLOR_BLUE}{task[0]}{COLOR_RESET}. {task[1]}.{COLOR_BOLD} {task[2]}{COLOR_RESET}"
        )