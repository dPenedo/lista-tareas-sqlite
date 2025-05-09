import sqlite3


def mark_as_completed(conn: sqlite3.Connection, id_task: int):
    cursor = conn.cursor()
    _ = cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id_task,))
    conn.commit()
    print("Task marked as completed.")
