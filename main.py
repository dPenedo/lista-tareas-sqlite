import sqlite3
from src import (
    mostrar_pendientes,
    mostrar_descripciones,
    marcar_completadas,
    mostrar_completadas,
    editar_tareas,
    inicializar_base_de_datos,
    eliminar_tareas,
    crear_tarea,
    obtener_datos,
)
import os


# Los colores
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"
COLOR_WHITE = "\033[37m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_RESET = "\033[0m"  # Reiniciar el color

BASE_DE_DATOS = "db/lista_de_tareas.db"


def mostrar_menu():
    print(f"{COLOR_BLUE}1.{COLOR_RESET} Crear una nueva tarea")
    print(f"{COLOR_BLUE}2.{COLOR_RESET} Marcar tarea como completada")
    print(f"{COLOR_BLUE}3.{COLOR_RESET} Editar una tarea pendiente")
    print(f"{COLOR_BLUE}4.{COLOR_RESET} Mostrar descripciones de las tareas pendientes")
    print(f"{COLOR_BLUE}5.{COLOR_RESET} Mostrar tareas completadas")
    print(f"{COLOR_BLUE}6.{COLOR_RESET} Mostrar tareas pendientes para esta semana")
    print(f"{COLOR_BLUE}7.{COLOR_RESET} Eliminar una tarea pendiente")
    print(f"{COLOR_BLUE}8.{COLOR_RESET} TEST")
    print(f"{COLOR_BLUE}0.{COLOR_RESET} Salir")


def main():
    inicializar_base_de_datos.inicializar_base_de_datos(BASE_DE_DATOS)
    conn = sqlite3.connect(BASE_DE_DATOS)
    os.system("clear")
    print(
        f"\n{COLOR_BLUE}Hola! 👋  Bienvenido a tu Administrador de Tareas{COLOR_RESET}"
    )
    contenidos_a_mostrar = "simple"
    while True:
        print("\nEstas son las Tareas que tienes pendientes:\n")
        if contenidos_a_mostrar == "simple":
            mostrar_pendientes.mostrar_pendientes(conn)
        elif contenidos_a_mostrar == "descripcion":
            mostrar_descripciones.mostrar_descripciones(conn)
            contenidos_a_mostrar = "simple"
        print("\n╚" + "═" * 48 + "╝")
        print("╔" + "═" * 48 + "╗")
        print(f"\n{COLOR_BLUE_TITLE}¿Qué deseas hacer?{COLOR_RESET}")
        mostrar_menu()
        opcion = input()
        if opcion == "1":
            print("Perfecto, vamos a crear una nueva tarea")
            print(
                "Son necesarios los siguientes valores: \n- Nombre \n- Descripción de la tarea\n- Fecha límite de la tarea"
            )
            print(f"\n{COLOR_BOLD}***************************{COLOR_RESET}\n")
            nombre, descripcion, fecha_limite = obtener_datos.obtener_tarea_nueva()
            crear_tarea.crear_tarea(conn, nombre, descripcion, fecha_limite)

            os.system("clear")
            print("Tarea Creada!")
        elif opcion == "2":
            seleccion = obtener_datos.obtener_tarea_seleccionada()
            marcar_completadas.marcar_completada(conn, seleccion)
            os.system("clear")
        elif opcion == "3":
            os.system("clear")
            editar_tareas.editar_tareas(conn)
        elif opcion == "4":
            os.system("clear")
            contenidos_a_mostrar = "descripcion"
            print("ahora van las de la semana")
        elif opcion == "5":
            os.system("clear")
            mostrar_completadas.mostrar_completadas(conn)
        elif opcion == "6":
            os.system("clear")
            print("Tareas pendientes de esta semana es una funcionalidad por hacer")
        elif opcion == "7":
            os.system("clear")
            eliminar_tareas.eliminar_tareas(conn)
        elif opcion == "8":
            os.system("clear")
            obtener_datos.obtener_tarea_seleccionada(conn)
        elif opcion == "0":
            print("🏃 Hasta pronto! ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    conn.close()


if __name__ == "__main__":
    main()
