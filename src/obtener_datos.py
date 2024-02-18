COLOR_BLUE = "\033[34m"
COLOR_RESET = "\033[0m"  # Reiniciar el color
COLOR_BOLD = "\033[1m"  # Negritas
from datetime import date
import os


def obtener_tarea_nueva():
    nombre = input(f"{COLOR_BLUE}Nombre de la tarea: {COLOR_RESET}")
    descripcion = input(f"{COLOR_BLUE}Descripción de la tarea: {COLOR_RESET}")
    fecha_limite = obtener_fecha()
    return nombre, descripcion, fecha_limite 

# TODO: Funciona, pero falta hacerle test e implementarlo
def obtener_tarea_seleccionada(conn):
    while True:
        try:
            print("Estas son las tareas almacenadas:")
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, descripcion, fecha_limite FROM tareas")
            tareas_pendientes = cursor.fetchall()
            for tarea in tareas_pendientes:
                print(f"{COLOR_BLUE}{tarea[0]}{COLOR_RESET}. {tarea[1]}.{COLOR_BOLD} {tarea[2]}{COLOR_RESET} ({tarea[3]})")
            seleccion = int(input("Seleccione el número de una tarea:\n"))
            tarea_encontrada = None
            for tarea in tareas_pendientes:
                if tarea[0] == seleccion:
                    tarea_encontrada = tarea
                    break
            if tarea_encontrada is None:
                raise ValueError("La tarea seleccionada no se encuentra en la lista")
            print(f"La Tarea encontrada es la número {tarea_encontrada[0]}: {tarea_encontrada[1]}")
            return tarea_encontrada
        except ValueError as e:
            os.system("clear")
            print(f"Error: {e}. Por favor, introduzca una tarea válida")

def obtener_fecha():
    hoy = date.today()
    print(f"Hoy es {hoy.day} del {hoy.month} del año {hoy.year}")

    while True:
        try:
            dia_limite = int(input(f"{COLOR_BLUE}Fecha limite: \n\tDía: {COLOR_RESET}"))
            if not 1 <= dia_limite <= 31:
                raise ValueError("El día debe estar entre 1 y 31")

            mes_limite = int(input(f"{COLOR_BLUE}\tMes: {COLOR_RESET}"))
            if not 1 <= mes_limite <= 12:
                raise ValueError("El mes debe estar entre 1 y 12")

            ano_limite = int(input(f"{COLOR_BLUE}\tAño: {COLOR_RESET}"))
            if ano_limite < 2024:
                raise ValueError("El año debe ser igual o posterior a 2024")
            fecha_limite = date(ano_limite, mes_limite, dia_limite)
            if fecha_limite == hoy:
                print("Es para hoy!")
            elif fecha_limite < hoy:
                print("Esa fecha ya ha pasado! Ingresa una fecha válida")
                continue
            else:
                print(f"Tarea programada para el {fecha_limite.day} del {fecha_limite.month} del {fecha_limite.year}")
            fecha_limite_reformateada = f"{dia_limite}/{mes_limite}/{ano_limite}"
            return (fecha_limite)
        except ValueError as e:
            print(f"Error: {e}. Por favor, introduzca una fecha válida.")

