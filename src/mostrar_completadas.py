COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"


def mostrar_completadas(conn):
    print(
        f"Aquí van las tareas que ya han sido{COLOR_BOLD} completadas{COLOR_RESET} con sus descripciones:"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion FROM tareas where completada = 1")
    tareas_pendientes = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Completadas:{COLOR_RESET}")
    for tarea in tareas_pendientes:
        print(f"{COLOR_BLUE}{tarea[0]}{COLOR_RESET}. {tarea[1]}. {tarea[2]}")
