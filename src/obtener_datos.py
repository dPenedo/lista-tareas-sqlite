COLOR_BLUE = "\033[34m"
COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BOLD = "\033[1m"  # Negritas


def obtener_tarea_nueva():
    nombre = input(f"{COLOR_BLUE}Nombre de la tarea: {COLOR_RESET}")
    descripcion = input(f"{COLOR_BLUE}Descripción de la tarea: {COLOR_RESET}")
    dia_limite = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
    mes_limite = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
    ano_limite = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
    # TODO: validacion de fechas
    fecha_limite = f"{ano_limite:04d}-{mes_limite:02d}-{dia_limite:02d}"
    return nombre, descripcion, fecha_limite 

def obtener_tarea_seleccionada():
    seleccion = input("Seleccione el número de una tarea:\n")
    # TODO: validacion de fechas
    return seleccion


