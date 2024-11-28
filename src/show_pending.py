COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"

COLOR_UNDERLINE = "\033[4m"  # Subrayado


def show_pending(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM tareas WHERE completada = 0")
    pending_tasks = cursor.fetchall()

    print(f"{COLOR_BLUE_TITLE}Pending tasks:{COLOR_RESET}")
    for tarea in pending_tasks:
        print(f"{COLOR_BLUE}{tarea[0]}{COLOR_RESET}. {tarea[1]}")
