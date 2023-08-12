COLOR_BLUE = "\033[34m"
COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BOLD = "\033[1m"  # Negritas


def crear_tarea(conn):
    print("Perfecto, vamos a crear una nueva tarea")
    print("Son necesarios los siguientes valores: \n- Nombre \n- Descripción de la tarea\n- Fecha límite de la tarea")
    print(f"\n{COLOR_BOLD}***************************{COLOR_RESET}\n")
    nombre = input(f"{COLOR_BLUE}Nombre de la tarea: {COLOR_RESET}")
    descripción = input(f"{COLOR_BLUE}Descripción de la tarea: {COLOR_RESET}")
    try:
        dia_limite = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
        mes_limite = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
        ano_limite = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
        fecha_limite = f"{ano_limite:04d}-{mes_limite:02d}-{dia_limite:02d}"
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?,?,?)", (nombre, descripción, fecha_limite))
        conn.commit()
        print("Se ha ingresado una nueva tarea!")
    except ValueError:
        print("Error: Ingresa un valor numérico válido para día, mes y año.")

    # print(nombre)
    # print(descripción)
    # print(fecha_limite)
