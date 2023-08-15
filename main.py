import sqlite3
import mostrar_pendientes
import mostrar_descripciones
import marcar_completadas 
import mostrar_completadas
import modificar_tareas
import eliminar_tareas
import crear_tarea
import os


# Los colores
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"
COLOR_WHITE = "\033[37m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_RESET = "\033[0m"  # Reiniciar el color

def mostrar_menu():
    print(f"{COLOR_BLUE}1.{COLOR_RESET} Mostrar descripciones de las tareas pendientes")
    print(f"{COLOR_BLUE}2.{COLOR_RESET} Marcar tarea como completada")
    print(f"{COLOR_BLUE}3.{COLOR_RESET} Crear una nueva tarea")
    print(f"{COLOR_BLUE}4.{COLOR_RESET} Mostrar tareas completadas")
    print(f"{COLOR_BLUE}5.{COLOR_RESET} Mostrar tareas pendientes para esta semana")
    print(f"{COLOR_BLUE}6.{COLOR_RESET} Editar una tarea pendiente")
    print(f"{COLOR_BLUE}7.{COLOR_RESET} Eliminar una tarea pendiente")
    print(f"{COLOR_BLUE}0.{COLOR_RESET} Salir")

def main():
    conn = sqlite3.connect('lista_de_tareas.db')
    os.system("clear")
    print(f"\n{COLOR_BLUE}Hola! 👋  Bienvenido a tu Administrador de Tareas{COLOR_RESET}")
    contenidos_a_mostrar = "simple"
    while True:
        print("\nEstas son las Tareas que tienes pendientes:\n") 
        if (contenidos_a_mostrar == "simple"):
            mostrar_pendientes.mostrar_pendientes(conn)
        elif (contenidos_a_mostrar == "descripcion"):
            mostrar_descripciones.mostrar_descripciones(conn)
            contenidos_a_mostrar = "simple"
        print("\n╚" + "═" * 48 + "╝")
        print("╔" + "═" * 48 + "╗")
        print(f"\n{COLOR_BLUE_TITLE}¿Qué deseas hacer?{COLOR_RESET}")
        mostrar_menu()
        opcion = input()
        if opcion == "1":
            os.system("clear")
            contenidos_a_mostrar = "descripcion"
            # mostrar_pendientes.mostrar_pendientes(conn)
            # print(f"\n{COLOR_BLUE_TITLE}¿Y ahora?¿Qué deseas hacer?{COLOR_RESET}")
        elif opcion == "2":
            marcar_completadas.marcar_completada(conn, input("Ingrese el número de la tarea a marcar como completada: "))
            os.system("clear")
        elif opcion == "3":
            crear_tarea.crear_tarea(conn)
            os.system("clear")
            print("Tarea Creada!")
        elif opcion == "4":
            os.system("clear")
            mostrar_completadas.mostrar_completadas(conn)
            print("ahora van las de la semana")
        elif opcion == "6":
            os.system("clear")
            modificar_tareas.modificar_tareas(conn)
        elif opcion == "7":
            os.system("clear")
            eliminar_tareas.eliminar_tareas(conn)
        elif opcion == "0":
            print("🏃 Talué! ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    conn.close()

if __name__ == "__main__":
    main()
