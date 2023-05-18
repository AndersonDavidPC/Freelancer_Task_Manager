#Importar métodos de otros archivos
from app.methods.register_task import registrar_tarea
from app.methods.show_tasks import mostrar_tareas
from app.methods.modify_task import modificar_tarea
from app.methods.show_debt_by_id import mostrar_deuda_por_id
from app.methods.delete_task import eliminar_tarea

# Menú principal
def ejecutar_menu():
    while True:
        print("1. Registrar una tarea")
        print("2. Mostrar todas las tareas")
        print("3. Modificar tarea")
        print("4. Mostrar deuda por ID")
        print("5. Eliminar tarea")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            modificar_tarea()
        elif opcion == "4":
            mostrar_deuda_por_id()
        elif opcion == "5":
            eliminar_tarea()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
