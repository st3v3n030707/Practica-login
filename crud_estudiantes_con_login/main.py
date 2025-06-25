from login import iniciar_sesion

def menu():
    print("=== Menú Principal ===")
    print("Aquí va el sistema CRUD de estudiantes")

# Ejecutar login antes de mostrar el menú
if iniciar_sesion():
    menu()
else:
    print("Saliendo del programa.")
