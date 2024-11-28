COLOR_RESET = "\033[0m"  # Reset color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Bold text
COLOR_BLUE_TITLE = "\033[34;1;4m"  # Blue, bold, underlined

def show_completed(conn):
    print(
        f"Here are the tasks that have been{COLOR_BOLD} completed{COLOR_RESET}, along with their descriptions:"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion FROM tareas WHERE completada = 1")
    completed_tasks = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Completed Tasks:{COLOR_RESET}")
    for task in completed_tasks:
        print(f"{COLOR_BLUE}{task[0]}{COLOR_RESET}. {task[1]}. {task[2]}")