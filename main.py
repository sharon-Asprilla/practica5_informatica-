#aqui se llaman todas las funciones que se haga 
import funciones as fc

usuarios = {}
fc.cargar_datos()

fc.archivo_usuarios()

"""
while True:
    fc.mensaje_bienvenida() 
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        contraseña = input("Contraseña: ")
        exito, msg = fc.iniciar_sesion(nombre, contraseña, usuarios)
        print(msg)
        if exito:
            print("Bienvenido a la red social!")
            break  # o continuar 
    elif opcion == "2":
        nombre = input("Nombre: ")
        contraseña = input("Contraseña: ")
        msg = fc.registrar_usuario(nombre, contraseña, usuarios)
        print(msg)
        
        continue  # repetir menu
    elif opcion == "3":
        print("")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
"""