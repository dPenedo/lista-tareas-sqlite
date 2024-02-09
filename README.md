### ¿Para qué sirve este script?

Este es un script para pruebas sencillas de python y sqlite. Está pensado como un recurso didáctico más que para uso práctico. De manera que sirve, básicamente para repasar, aprender y practicar y la he puesto como pública por si le es de utilidad a alguien en ese sentido.

### ¿En qué consiste?

La idea es que cree una base de datos simple de tareas e ir agregando opciones para mostrarlas, marcarlas como leídas, editarlas, etc. Toda la interacción se dará desde la consola de comandos al ejecutar `python main.py` y la idea es utilizar el mínimo de bibliotecas posible para ir utilizando los propios comandos sqlite desde el script. De momento tiene las siguientes funciones:

- Crear tareas
- Mostrar tareas ya completadas
- Marcar una tarea como completada
- Mostrar descripciones de todas las tareas
- Editar una tarea pendiente (editándola por completo o un sólo parámetro)
- Eliminar una tarea pendiente (con una confirmación previa)


### ¿Cómo lo puedes utilizar?

Para utilizarlo en tu dispositivo sigue los siguientes pasos:
- Clona este repositorio y entra en él:
``` bash
git clone https://github.com/dPenedo/lista-tareas-sqlite
cd lista-tareas-sqlite
```

Inicia este script:
``` bash
python main.py
```

### Funciones por hacer

- Validación de fechas
- Comprobar las tareas por hacer esta semana
- Comprobar las tareas por hacer este mes
- Testing: probar funciones con unittest
