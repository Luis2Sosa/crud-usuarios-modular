# Para ver la lista de usuarios en pantalla y el archivo en modo lectura
def ver_usuarios():
    print("--> Usuarios a mostrar: <--")
    with open("data/usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        if not lineas:
            print("No hay usuarios a mostrar.")
        else:
            for linea in lineas:
                    datos = linea.strip().split(",")
                    if len(datos) == 3:
                        nombre = datos[0]
                        edad = datos[1]
                        correo = datos[2]
                
                        print("Nombre:", nombre)
                        print("Edad:", edad)
                        print("Correo:", correo)
                        print("-" * 45)