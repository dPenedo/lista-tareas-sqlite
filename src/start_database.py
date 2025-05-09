import sqlite3


def start_database(database: str):
    """Inicializa la base de datos y la crea si no existe"""
    try:
        conn = sqlite3.connect(database)
        with conn:
            cursor = conn.cursor()
            _ = cursor.execute(
                """CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    completada INTEGER DEFAULT 0,
                    fecha_limite DATE
                )"""
            )
            print("Database created successfully")
            return conn

    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")
        return None
