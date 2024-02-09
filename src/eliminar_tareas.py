import os

COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"

def eliminar_tareas(conn):
    print(f"{COLOR_BOLD}¿Qué tarea quieres eliminar?{COLOR_RESET}\n")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion, fecha_limite FROM tareas where completada = 0")
    tareas_pendientes = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Tareas a eliminar:{COLOR_RESET}")
    for tarea in tareas_pendientes:
        print(f"{COLOR_BLUE}{tarea[0]}{COLOR_RESET}. {tarea[1]}.{COLOR_BOLD} {tarea[2]}{COLOR_RESET} ({tarea[3]})")
    tarea_elegida = int(input("Selecciona el número: "))

    tarea_encontrada = None

    for tarea in tareas_pendientes:
        if tarea[0] == tarea_elegida:
            tarea_encontrada = tarea
            break

    if tarea_encontrada:
        print(f"La tarea elegida es:{COLOR_BOLD}{tarea_encontrada[1]}{COLOR_RESET}")
        print(f"{COLOR_BOLD}  ¿Estás seguro de que la quieres eliminar?{COLOR_RESET}")
        continuar = input("Pulsa \"s\" si quieres eliminarla o cualquier tecla para volver al menú principal\n")
        if continuar == "s":
            cursor.execute("DELETE FROM tareas WHERE id = ? ", (tarea_encontrada[0],))
            os.system("clear")
            print(f"la tarea {tarea_encontrada[1]} ha sido eliminada")
        else:
            os.system("clear")
            print("Volver al inicio")
        
    else:
        print("No se ha encontrado la tarea")
