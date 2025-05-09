import os
import sqlite3

from src.ui.colorize import Color, colorize

COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"


def edit_task(conn: sqlite3.Connection):
    # TODO: externalizar a obtener_datos los siguientes datos
    # Datos:
    # id_seleccion
    # nombre
    # descripcion
    # fecha_limite

    print(colorize("¿Qué tarea quieres modificar?", Color.BOLD))
    cursor = conn.cursor()
    _ = cursor.execute(
        "SELECT id, nombre, descripcion, fecha_limite FROM tareas where completada = 0"
    )
    pending_tasks: list[tuple[int, str, str, str]] = cursor.fetchall()
    print(colorize("Tareas a modificar:", Color.BLUETITLE))
    for task in pending_tasks:
        print(
            f"{colorize(str(task[0]), Color.BLUE)}. {task[1]}.{colorize(task[2], Color.BOLD)} ({task[3]})"
        )
    chosen_task = int(input("Selecciona el número: "))  # id_seleccion

    found_task = None

    for task in pending_tasks:
        if task[0] == chosen_task:
            found_task = task
            break

    if found_task:
        print(f"La tarea elegida es:{colorize(found_task[1], Color.BOLD)}")

        print(colorize("¿Y qué quieres modificar?", Color.BOLD))
        print(f"{colorize("1.", Color.BLUE)} El nombre de la Tarea")
        print(f"{colorize("2.", Color.BLUE)} La descripción de la tarea")
        print(f"{colorize("3.", Color.BLUE)} La fecha limite")
        print(f"{colorize("4.", Color.BLUE)} Todo")
        print(
            f"{COLOR_BLUE}Cualquier tecla.{COLOR_RESET} Nada, quiero volver al menú inicial"
        )
        found_column = input("¿Qué quieres modificar? ")
        if found_column == "1":
            name = input("\n¿Qué nuevo nombre quieres darle? ")  # nombre
            _ = cursor.execute(
                "UPDATE tareas SET nombre= ?  WHERE id = ?",
                (name, found_task[0]),
            )
            conn.commit()
            print("El nombre ha sido modificado")

        elif found_column == "2":
            description = input(
                "\n¿Qué nueva descripción quieres darle?"
            )  # descripcion
            _ = cursor.execute(
                "UPDATE tareas SET descripcion= ?  WHERE id = ?",
                (description, found_task[0]),
            )
            conn.commit()
            print("La descripción ha sido modificado")
        elif found_column == "3":
            day_deadline = int(
                input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}")
            )
            month_deadline = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            year_deadline = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            date_deadline = f"{year_deadline:04d}-{month_deadline:02d}-{day_deadline:02d}"  # fecha_limite
            _ = cursor.execute(
                "UPDATE tareas SET fecha_limite= ?  WHERE id = ?",
                (date_deadline, found_task[0]),
            )
            conn.commit()
            print("La fecha límite ha sido modificada")
        elif found_column == "4":
            name = input("\n¿Qué nuevo nombre quieres darle? ")  # nombre
            description = input(
                "\n¿Qué nueva descripción quieres darle?"
            )  # descripcion
            day_deadline = int(
                input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}")
            )
            month_deadline = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            year_deadline = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            date_deadline = f"{year_deadline:04d}-{month_deadline:02d}-{day_deadline:02d}"  # fecha_limite
            _ = cursor.execute(
                "UPDATE tareas SET nombre= ?, descripcion= ? , fecha_limite = ?  WHERE id = ?",
                (name, description, date_deadline, found_task[0]),
            )
            conn.commit()
            print("El nombre, la descripcion y a fecha limite han sido modificados")
        else:
            _ = os.system("clear")
            pass

    else:
        print("No se ha encontrado la tarea")
