import sqlite3


class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db

    def init_db(self):
        """Inicializa la base de datos y la crea si no existe"""
        try:
            conn = sqlite3.connect(database)
            cursor = self.connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    completada INTEGER DEFAULT 0,
                    fecha_limite DATE
                )"""
            )
            conn.commit()
            print("Database created successfully")
            return conn

        except sqlite3.Error as e:
            print(f"Error creating the database: {e}")
            return None
