import sqlite3
import mostrar_pendientes
import marcar_completadas 
import crear_nota
import os


# Los colores
COLOR_BLUE = "\033[34m"
COLOR_BLUE_TITLE = "\033[34;1;4m"
COLOR_WHITE = "\033[37m"
COLOR_BOLD = "\033[1m"  # Negritas
COLOR_RESET = "\033[0m"  # Reiniciar el color

def mostrar_menu():
    print(f"{COLOR_BLUE}1.{COLOR_RESET} Volver a mostrar tareas pendientes")
    print(f"{COLOR_BLUE}2.{COLOR_RESET} Marcar tarea como completada")
    print(f"{COLOR_BLUE}3.{COLOR_RESET} Crear una nueva tarea")
    print(f"{COLOR_BLUE}4.{COLOR_RESET} Mostrar tareas pendientes para esta semana")
    print(f"{COLOR_BLUE}0.{COLOR_RESET} Salir")

def main():
    conn = sqlite3.connect('lista_de_tareas.db')
    os.system("clear")
    while True:
        print(f"\n{COLOR_BLUE}Hola! 👋  Bienvenido a tu Administrador de Tareas{COLOR_RESET}")
        print("\nEstas son las Tareas que tienes pendientes:\n") 
        mostrar_pendientes.mostrar_pendientes(conn)
        print(f"\n{COLOR_BOLD}***************************{COLOR_RESET}")
        print(f"{COLOR_BOLD}***************************{COLOR_RESET}\n")
        print(f"{COLOR_BLUE_TITLE}¿Qué deseas hacer?{COLOR_RESET}")
        mostrar_menu()
        opcion = input()
        if opcion == "1":
            print("Ahí van de nuevo:")
            mostrar_pendientes.mostrar_pendientes(conn)
            print(f"\n{COLOR_BLUE_TITLE}¿Y ahora?¿Qué deseas hacer?{COLOR_RESET}")
        elif opcion == "2":
            marcar_completadas.marcar_completada(conn, input("Ingrese el número de la tarea a marcar como completada: "))
        elif opcion == "3":
            crear_nota.crear_nota(conn)
        elif opcion == "4":
            print("ahora van las de la semana")
        elif opcion == "0":
            print("🏃 Talué! ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    conn.close()

if __name__ == "__main__":
    main()
