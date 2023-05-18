# Freelancer Task Manager

El Freelancer Task Manager es una herramienta simple para registrar y administrar tareas de clientes para trabajadores freelancers. Permite realizar un seguimiento de las tareas, el estado, los pagos y la deuda de los clientes.

## Características

- Registro de tareas: Permite registrar nuevas tareas con información como el nombre de la tarea, la fecha de vencimiento, el precio acordado, el monto pagado y el estado.
- Modificación de tareas: Permite modificar el estado y el monto pagado de una tarea existente.
- Visualización de deuda por cliente: Permite verificar la cantidad adeudada por un cliente específico.
- Listado de tareas: Muestra todas las tareas registradas con su información relevante.
-Eliminación de tareas: Permite eliminar una tarea existente.


## Instrucciones de uso

1. Clona o descarga el repositorio del Freelancer Task Manager.
2. Asegúrate de tener instalado Python en tu sistema.
3. Desde la línea de comandos, navega hasta el directorio del proyecto.
4. Ejecuta el script principal `main.py` con Python.
5. Sigue las instrucciones en el menú principal para realizar diferentes acciones, como registrar una tarea, modificar una tarea, ver la deuda por cliente, etc.
6. Los datos de las tareas se almacenan en el archivo `data/tasks.csv`, y los datos de los clientes se almacenan en el archivo `data/customers.csv`. Asegúrate de que estos archivos existan y tengan los permisos adecuados para lectura y escritura.

## Ejemplo de estructura de archivos

```
main.py
README.md
data/
  |- tasks.csv
  |- customers.csv
app/
  |- methods/
    |- modify_tasks.py
    |- register_task.py
    |- show_debt_by_id.py
    |- show_tasks.
    |- delete_task.py
```

## Contribución

Si deseas contribuir al Freelancer Task Manager, puedes seguir los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza los cambios y realiza commits descriptivos.
4. Realiza un push a tu rama: `git push origin feature/nueva-funcionalidad`.
5. Crea un pull request en el repositorio original.

## Notas

- El Freelancer Task Manager es una herramienta simple y puede requerir ajustes o mejoras adicionales según tus necesidades específicas.
- Asegúrate de realizar copias de seguridad de los archivos CSV regularmente para evitar la pérdida de datos.
- Este proyecto se proporciona como está y no ofrece garantía de ningún tipo.

## Licencia

Este proyecto está bajo la licencia [MIT License](https://opensource.org/licenses/MIT).