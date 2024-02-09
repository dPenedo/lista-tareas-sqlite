import os
import sqlite3

def inicializar_base_de_datos():
    try:
        conn = sqlite3.connect('db/lista_de_tareas.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            descripcion TEXT,
                            completada INTEGER DEFAULT 0,
                            fecha_limite DATE
                        )''')
        conn.commit()
        print("Base de datos creada exitosamente")
   
    except sqlite3.Error as e:
        print("Error al crear la base de datos")

    finally:
        if conn:
            conn.close()
    
