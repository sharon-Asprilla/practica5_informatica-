#aqui se implementa toda la logica de la aplicacion en funciones 
import datetime as dt

def mensaje_bienvenida():
    print("****************************************")
    print("*   la Red Social    *")
    print("****************************************")
    print("1. iniciar sesion")
    print("2. registrarse")
    print
    print("3. salir")



def archivo_usuarios():
    with open ("users.txt", "r",encoding="utf-8") as archivo:
        usuario = {}
        nombre = ""
        contraseña = ""
        nombre = ""
        contraseña=""
        for linea in archivo:
            for fila in linea:
                if ";" in linea:
                    nombre, contraseña = linea.split(";")
                    usuario[nombre] = {
                        "contraseña": contraseña
                    }
    return usuario

print(archivo_usuarios())
print()
print()


def cargar_datos():
    usuarios = {}
    nombre = None

    with open("userData.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:   # recorremos cada línea
            linea = linea.strip()

            # Si la línea tiene un * → nombre y amigos
            if "*" in linea:
                partes = linea[1:].split(":")   # quitamos el *
                nombre = partes[0]              # el primer dato es el nombre
                amigos = partes[1].split(",") if len(partes) > 1 else []  # después de : vienen los amigos
                usuarios[nombre] = {
                    "amigos": amigos,
                    "gustos": [],
                    "mensajes": []
                }

            # Si la línea tiene { → gustos
            if "{" in linea:
                gustos = linea[1:-1].split(",")
                usuarios[nombre]["gustos"] = gustos

            # Si la línea tiene "El "  es mensajes
            if "El " in linea:
                usuarios[nombre]["mensajes"].append(linea)

    return usuarios


# Probar
datos = cargar_datos()
print(datos)


    









