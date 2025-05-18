# Importamos la fecha 
from datetime import datetime

# Una funcion para modificar el usuario y ponerle nueva fecha
def modificar_usuario():
    print("--> Modificar usuario <--")
    nombre_a_modificar = input("Ingrese el nombre del usuario que quiere modificar:\n").lower().strip()
    
    with open("data/usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        nuevas_lineas = []
        usuario_encontrado = False
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d_%H-%M-%S")
        
        for linea in lineas:
            datos = linea.strip().split(",")
            nombre = datos[0]
            
            # Si coinciden pedimos los nuevos datos
            if nombre == nombre_a_modificar:
                nueva_edad = input("Ingrese la nueva edad del usuario:\n").strip()
                nuevo_correo = input("Ingrese el nuevo correo del usuario:\n").lower().strip()
                if "@" not in nuevo_correo or "." not in nuevo_correo:
                    print("Nuevo correo no permitido.")
                else:
                    nueva_linea = f"{nombre},{nueva_edad},{nuevo_correo},{fecha}\n"
                    nuevas_lineas.append(nueva_linea)
                    usuario_encontrado = True
                
        # Agregamos el nuevo archivo
        with open("data/usuarios.txt", "w") as archivo:
            archivo.writelines(nuevas_lineas)
        
        if usuario_encontrado:
            print("Usuario modificado correctamente.")
        else:
            print("Usuario no")