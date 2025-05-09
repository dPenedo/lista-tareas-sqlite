import sqlite3


def create_task(
    conn: sqlite3.Connection, nombre: str, descripcion: str, fecha_limite: str
):
    """
    Inserts a new task into the 'tareas' table.

    Parameters:
        conn (sqlite3.Connection): The database connection.
        nombre (str): The task's name.
        descripcion (str): The task's description.
        fecha_limite (str): The task's deadline in 'YYYY-MM-DD' format.

    Returns:
        bool: True if the task was inserted successfully, False otherwise.
    """
    try:
        cursor = conn.cursor()
        _ = cursor.execute(
            "INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?, ?, ?)",
            (nombre, descripcion, fecha_limite),
        )
        conn.commit()
        print("A new task has been added!")
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
