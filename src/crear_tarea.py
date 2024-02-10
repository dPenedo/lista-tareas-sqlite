
# TODO: para poder probar la funcion de crear tareas hay que refactorizar para que los inputs sean dados por parametros
def crear_tarea(conn, nombre, descripcion, fecha_limite):
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO tareas (nombre, descripcion, fecha_limite) VALUES (?,?,?)", (nombre, descripcion, fecha_limite))
        conn.commit()
        print("Se ha ingresado una nueva tarea!")
        return True
    except ValueError:
        print("Error: Ingresa un valor numérico válido para día, mes y año.")
        return False


    # print(nombre)
    # print(descripción)
    # print(fecha_limite)
