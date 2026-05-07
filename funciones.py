#aqui se implementa toda la logica de la aplicacion en funciones 
import datetime as dt

def mensaje_bienvenida():
    print("****************************************")
    print("*   Bienvenido a la Red Social    *")
    print("****************************************")
    print("1. iniciar sesion")
    print("2. registrarse")
    print("3. salir")

    pass
# diccionario vacio para poder acceder a el e ir agregando
usuarios = {}

def registrar_usuario(nombre, contraseña):
    if not nombre.isalpha(): #verifica si es valido lo que ingresa el usuario
        return False, "El nombre debe ser solo texto"
    if nombre in usuarios: # si nombre esta en usuarios
        return False, "El usuario ya existe." # si no retorna  un falso y da un mensaje
    usuarios[nombre] = { # luego crea un diccionario con la clave nombre y se le da el nombre alas claves 
        "contraseña": contraseña,#y lo demas es listas vacias
        "amigos": [],
        "solicitudes": [],
        "gustos": [],
        "mensajes": []
    }# todo siendo un diccionario solo

    # Guardar en archivo users.txt
    with open("users.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre};{contraseña}\n")
    return True




