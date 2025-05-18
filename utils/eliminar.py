# La funcion eliminar usuario si lo encuentra no lo deja pasar y agrega los demás a la lista
def eliminar_usuario():
    print("--> Eliminar usuario <---")
    nombre_a_borrar = input("Ingrese el nombre del usuario que quiere eliminar:\n").lower().strip()
    with open("data/usuarios.txt", "r") as archivo:
        lineas = archivo.readlines()
        nuevas_lineas = []
        usuario_encontrado = False
        
        for linea in lineas:
            datos = linea.strip().split(",")
            nombre = datos[0]
            
            if nombre == nombre_a_borrar:
                usuario_encontrado = True
            else:
                nuevas_lineas.append(linea)
        
        with open("data/usuarios.txt", "w") as archivo:
            archivo.writelines(nuevas_lineas)
            
        if usuario_encontrado:
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")