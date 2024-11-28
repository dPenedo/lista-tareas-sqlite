import os

COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BLUE = "\033[34m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_BLUE_TITLE = "\033[34;1;4m"


def edit_task(conn):
    # TODO: externalizar a obtener_datos los siguientes datos
    # Datos:
    # id_seleccion
    # nombre
    # descripcion
    # fecha_limite

    print(f"{COLOR_BOLD}¿Qué tarea quieres modificar?{COLOR_RESET}\n")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nombre, descripcion, fecha_limite FROM tareas where completada = 0"
    )
    pendint_tasks = cursor.fetchall()
    print(f"{COLOR_BLUE_TITLE}Tareas a modificar:{COLOR_RESET}")
    for task in pendint_tasks:
        print(
            f"{COLOR_BLUE}{task[0]}{COLOR_RESET}. {task[1]}.{COLOR_BOLD} {task[2]}{COLOR_RESET} ({task[3]})"
        )
    chosen_task = int(input("Selecciona el número: "))  # id_seleccion

    found_task = None

    for task in pendint_tasks:
        if task[0] == chosen_task:
            found_task = task
            break

    if found_task:
        print(f"La tarea elegida es:{COLOR_BOLD}{found_task[1]}{COLOR_RESET}")
        print(f"{COLOR_BOLD}¿Y qué quieres modificar?{COLOR_RESET} \n")
        print(f"{COLOR_BLUE}1.{COLOR_RESET} El nombre de la Tarea")
        print(f"{COLOR_BLUE}2.{COLOR_RESET} La descripción de la tarea")
        print(f"{COLOR_BLUE}3.{COLOR_RESET} La fecha limite")
        print(f"{COLOR_BLUE}4.{COLOR_RESET} Todo")
        print(
            f"{COLOR_BLUE}Cualquier tecla.{COLOR_RESET} Nada, quiero volver al menú inicial"
        )
        found_column = input("¿Qué quieres modificar? ")
        if found_column == "1":
            name = input("\n¿Qué nuevo nombre quieres darle? ")  # nombre
            cursor.execute(
                "UPDATE tareas SET nombre= ?  WHERE id = ?",
                (name, found_task[0]),
            )
            conn.commit()
            print("El nombre ha sido modificado")

        elif found_column == "2":
            description = input(
                "\n¿Qué nueva descripción quieres darle?"
            )  # descripcion
            cursor.execute(
                "UPDATE tareas SET descripcion= ?  WHERE id = ?",
                (description, found_task[0]),
            )
            conn.commit()
            print("La descripción ha sido modificado")
        elif found_column == "3":
            day_deadline = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
            month_deadline = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            year_deadline = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            date_deadline = (
                f"{year_deadline:04d}-{month_deadline:02d}-{day_deadline:02d}"  # fecha_limite
            )
            cursor.execute(
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
            day_deadline = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
            month_deadline = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            year_deadline = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            date_deadline = (
                f"{year_deadline:04d}-{month_deadline:02d}-{day_deadline:02d}"  # fecha_limite
            )
            cursor.execute(
                "UPDATE tareas SET nombre= ?, descripcion= ? , fecha_limite = ?  WHERE id = ?",
                (name, description, date_deadline, found_task[0]),
            )
            conn.commit()
            print("El nombre, la descripcion y a fecha limite han sido modificados")
        else:
            os.system("clear")
            pass

    else:
        print("No se ha encontrado la tarea")
