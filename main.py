import sqlite3
import completar_tarea

def main():
    conn = sqlite3.connect('lista_de_tareas.db')
    
    completar_tarea.mostrar_tareas_pendientes(conn)
    
    id_tarea = input("Ingrese el número de la tarea a marcar como completada: ")
    completar_tarea.marcar_completada(conn, id_tarea)
    
    conn.close()

if __name__ == "__main__":
    main()
