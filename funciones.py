#aqui se implementa toda la logica de la aplicacion en funciones 
import datetime as dt

def mensaje_bienvenida():
    print("****************************************")
    print("*   la Red Social    *")
    print("****************************************")
    print("1. iniciar sesion")
    print("2. registrarse")
    print("3. salir")

    
# diccionario vacio para poder acceder a el e ir agregando
usuarios = {}

def cargar_usuarios():
    with open("users.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if ";" in linea:
                nombre, contraseña = linea.strip().split(";")
                usuarios[nombre] = {
                    "contraseña": contraseña,
                    "amigos": [],
                    "solicitudes": [],
                    "gustos": [],
                    "mensajes": []
                }

def iniciar_sesion(nombre, contraseña, usuarios):
     # ve si esta el nombre en el diciconario
    if nombre in usuarios:
        # ver si la contraseña son iguales
        if usuarios[nombre]["contraseña"] == contraseña:
            return True, "Sesión iniciada correctamente."
        else:
            return False, "Contraseña incorrecta."
    else:
        return False, "Usuario no registrado."

def registrar_usuario(nombre, contraseña, usuarios):
    if not nombre.isalpha(): #verifica si es valido lo que ingresa el usuario
        return False, "El nombre debe ser solo texto"
    if nombre in usuarios and usuarios[nombre]["contraseña"] == contraseña:
        return False, "El usuario ya está registrado con esa contraseña, iniciar sesion porfavor"
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
    return True, "Usuario registrado correctamente."





