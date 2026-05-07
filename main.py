#aqui se llaman todas las funciones que se haga 
import funciones as fc

fc.mensaje_bienvenida() #llamada de funcion de la bienvenida

opcion = input("Seleccione una opcion: ")

if opcion == "1":
    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")
    msg = fc.registrar_usuario(nombre, contraseña)
    print

