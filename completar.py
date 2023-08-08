import sqlite3

def mostrar_tareas_pendientes(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM tareas WHERE completada = 0')
    tareas_pendientes = cursor.fetchall()

    print("Tareas pendientes:")
    for tarea in tareas_pendientes:
        print(f"{tarea[0]}. {tarea[1]}")

def marcar_completada(conn, id_tarea):
    cursor = conn.cursor()
    cursor.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (id_tarea,))
    conn.commit()
    print("Tarea marcada como completada.")

def main():
    conn = sqlite3.connect('lista_de_tareas.db')
    
    mostrar_tareas_pendientes(conn)
    
    id_tarea = input("Ingrese el número de la tarea a marcar como completada: ")
    marcar_completada(conn, id_tarea)
    
    conn.close()

if __name__ == "__main__":
    main()
