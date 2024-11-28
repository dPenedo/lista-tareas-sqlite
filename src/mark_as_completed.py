def mark_as_completed(conn, id_task):
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id_task,))
    conn.commit()
    print("Task marked as completed.")
