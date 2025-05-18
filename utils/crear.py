# Importamos la fecha
from datetime import datetime

# Creamos la funcion para crear usuario con la fecha y validamos el correo
def crear_usuario():
    print("--> Crear usuario <--")
    nombre = input("Ingrese el nombre del usuario:\n").lower().strip()
    edad = input("Ingrese la edad del usuario:\n").strip()
    correo = input("Ingrese el correo del usuario:\n").lower().strip()
    
    if "@" not in correo or "." not in correo:
        print("Correo no valido.")
    else:
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d_%H-%M-%S")
        
        linea = f"{nombre},{edad},{correo},{fecha}\n"
        with open("data/usuarios.txt", "a") as archivo:
            archivo.write(linea)
            print("Usuario creado correctamente.")
            

    