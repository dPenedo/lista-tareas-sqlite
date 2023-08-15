import mostrar_descripciones
import os

COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"

def modificar_tareas(conn):
    print(f"{COLOR_BOLD}¿Qué tarea quieres modificar?{COLOR_RESET}\n")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion, fecha_limite FROM tareas where completada = 0")
    tareas_pendientes = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Tareas a modificar:{COLOR_RESET}")
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
        print(f"{COLOR_BOLD}¿Y qué quieres modificar?{COLOR_RESET} \n")
        print(f"{COLOR_BLUE}1.{COLOR_RESET} El nombre de la Tarea")
        print(f"{COLOR_BLUE}2.{COLOR_RESET} La descripción de la tarea")
        print(f"{COLOR_BLUE}3.{COLOR_RESET} La fecha limite")
        print(f"{COLOR_BLUE}4.{COLOR_RESET} Todo")
        print(f"{COLOR_BLUE}Cualquier tecla.{COLOR_RESET} Nada, quiero volver al menú inicial")
        columna_elegida = input("¿Qué quieres modificar? ")
        if columna_elegida == "1":
            nombre = input("\n¿Qué nuevo nombre quieres darle? ")
            cursor.execute("UPDATE tareas SET nombre= ?  WHERE id = ?", (nombre, tarea_encontrada[0]))
            print("El nombre ha sido modificado")

        elif columna_elegida == "2":
            descripcion = input("\n¿Qué nueva descripción quieres darle?")
            cursor.execute("UPDATE tareas SET descripcion= ?  WHERE id = ?", (descripcion, tarea_encontrada[0]))
            print("La descripción ha sido modificado")
        elif columna_elegida == "3":
            dia_limite = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
            mes_limite = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            ano_limite = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            fecha_limite = f"{ano_limite:04d}-{mes_limite:02d}-{dia_limite:02d}"
            cursor.execute("UPDATE tareas SET fecha_limite= ?  WHERE id = ?", (fecha_limite, tarea_encontrada[0]))
            print("La fecha límite ha sido modificada")
        elif columna_elegida == "4":
            nombre = input("\n¿Qué nuevo nombre quieres darle? ")
            descripcion = input("\n¿Qué nueva descripción quieres darle?")
            dia_limite = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
            mes_limite = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            ano_limite = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            fecha_limite = f"{ano_limite:04d}-{mes_limite:02d}-{dia_limite:02d}"
            cursor.execute("UPDATE tareas SET nombre= ?, descripcion= ? , fecha_limite = ?  WHERE id = ?", (nombre, descripcion, fecha_limite, tarea_encontrada[0]))
            print("El nombre, la descripcion y a fecha limite han sido modificados")
        else:
            os.system("clear")
            pass


        
    else:
        print("No se ha encontrado la tarea")
