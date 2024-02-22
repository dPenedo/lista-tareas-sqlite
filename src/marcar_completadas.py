def marcar_completada(conn, id_tarea):
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id_tarea,))
    conn.commit()
    print("Tarea marcada como completada.")
