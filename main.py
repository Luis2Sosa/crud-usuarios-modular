# Importamos todos los archivos a utilizar
from utils.crear import crear_usuario
from utils.ver import ver_usuarios
from utils.modificar import modificar_usuario
from utils.eliminar import eliminar_usuario

# Creamos la funcion del menu con bienvenida
def menu():
    print("--- BIENVENIDO AL GESTOR DE USUARIOS ---\n")
    print("1. Crear usuario")
    print("2. Ver usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir\n")

# Creamos la funcion que iniciara el sistema hasta que el usuario decida salir    
def iniciar_sistema():
    while True:
        menu()
        opcion = input("Ingrese un numero de opción:\n").lower().strip()
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            print("Gracias por utilizar el Gestor de Usuarios.")
            break
        else:
            print("Opción no valida.")


# __name__ para que solo se llame iniciar sistema desde aquí            
if __name__ == "__main__":
    iniciar_sistema()