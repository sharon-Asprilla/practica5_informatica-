"""
funciones para la red social
Aquí están todas las funciones que maneja la información
"""
import datetime  # Importar datetime para los mensajes

def cargar_datos():
    """
    Carga todos los datos de ambos archivos
    Devuelve un diccionario con todos los usuarios
    """
    usuarios = {}  # Creamos diccionario vacío para guardar usuarios
    
    # PASO 1: Cargar nombres y contraseñas desde users.txt
    archivo = open("users.txt", "r")  # Abrimos archivo para leer
    for linea in archivo:  # Para cada línea del archivo
        linea = linea.strip()  # Eliminamos espacios en blanco
        if linea:  # Si la línea no está vacía
            # Dividimos la línea por punto y coma (nombre;password)
            partes = linea.split(";")  # Dividimos en dos partes
            nombre = partes[0]  # Primera parte es el nombre
            password = partes[1]  # Segunda parte es la contraseña
            
            # Creamos estructura para este usuario
            usuarios[nombre] = {  # Creamos entrada en el diccionario
                "password": password,  # Guardamos su contraseña
                "amigos": [],  # Lista vacía de amigos
                "solicitudes": [],  # Lista vacía de solicitudes
                "gustos": [],  # Lista vacía de gustos
                "mensajes": []  # Lista vacía de mensajes
            }
    archivo.close()  # Cerramos el archivo
    
    # PASO 2: Cargar información adicional desde userData.txt
      
    archivo = open("userData.txt", "r")  # Abrimos archivo para leer
    nombre_actual = ""  # Variable para guardar de quién es la información
    for linea in archivo:  # Para cada línea del archivo
        linea = linea.strip()  # Eliminamos espacios en blanco
        if linea:  # Si la línea no está vacía
            # Verificar el primer carácter manualmente
            primer_caracter = linea[0]  # Obtenemos el primer carácter
            
            # Si empieza con * es la línea de usuario y amigos
            if primer_caracter == "*":  # Si el primer carácter es asterisco
                linea = linea[1:]  # Quitamos el asterisco
                partes = linea.split(":")  # Dividimos por dos puntos
                nombre_actual = partes[0]  # El nombre es lo que viene antes de :
                
                if nombre_actual in usuarios:  # Si este usuario existe
                    if len(partes) > 1:  # Si hay información después del :
                        resto = partes[1] if len(partes) > 1 else ""  # Obtenemos lo que viene después del :
                        
                        # Buscamos si hay < (solicitudes)
                        hay_solicitudes = False  # Bandera para saber si hay solicitudes
                        posicion_menor = -1  # Posición del <
                        posicion_mayor = -1  # Posición del >
                        
                        # Buscamos manualmente el < en la cadena
                        for i in range(len(resto)):  # Para cada posición
                            if resto[i] == "<":  # Si encontramos <
                                posicion_menor = i  # Guardamos posición
                                hay_solicitudes = True  # Hay solicitudes
                                break  # Paramos de buscar
                        
                        # Si hay <, buscamos el >
                        if hay_solicitudes:  # Si encontramos <
                            for i in range(posicion_menor + 1, len(resto)):  # Desde < hacia adelante
                                if resto[i] == ">":  # Si encontramos >
                                    posicion_mayor = i  # Guardamos posición
                                    break  # Paramos
                            
                            # Dividimos en amigos y solicitudes
                            amigos_parte = ""  # Amigos antes del <
                            for i in range(posicion_menor):
                                amigos_parte = amigos_parte + resto[i]
                            solicitudes_parte = ""  # Entre < y >
                            for i in range(posicion_menor + 1, posicion_mayor):
                                solicitudes_parte = solicitudes_parte + resto[i]
                            
                            # Procesar amigos
                            amigos_limpio = ""  # Variable para limpiar
                            for caracter in amigos_parte:  # Para cada carácter
                                if caracter != " ":  # Si no es espacio
                                    amigos_limpio = amigos_limpio + caracter  # Agregamos
                            
                            # Quitar coma final si la hay
                            if len(amigos_limpio) > 0:  # Si hay algo
                                if amigos_limpio[-1] == ",":  # Si termina en coma
                                    amigos_limpio = amigos_limpio[:-1]  # Quitamos la coma
                            
                            if amigos_limpio:  # Si hay amigos
                                amigos = []  # Dividimos por coma
                                actual = ""
                                for c in amigos_limpio:
                                    if c == ",":
                                        if actual:
                                            amigos.append(actual)
                                        actual = ""
                                    else:
                                        actual = actual + c
                                if actual:
                                    amigos.append(actual)
                                usuarios[nombre_actual]["amigos"] = amigos
                            
                            # Procesar solicitudes
                            if solicitudes_parte:  # Si hay solicitudes
                                solicitudes = []  # Dividimos por coma
                                actual = ""
                                for c in solicitudes_parte:
                                    if c == ",":
                                        if actual:
                                            solicitudes.append(actual.strip())
                                        actual = ""
                                    else:
                                        actual = actual + c
                                if actual:
                                    solicitudes.append(actual.strip())
                                usuarios[nombre_actual]["solicitudes"] = solicitudes
                        else:  # Si no hay solicitudes
                            if resto:  # Si hay información de amigos
                                amigos_limpio = ""  # Variable para limpiar
                                for caracter in resto:  # Para cada carácter
                                    if caracter != " ":  # Si no es espacio
                                        amigos_limpio = amigos_limpio + caracter  # Agregamos
                                
                                # Quitar coma final si la hay
                                if len(amigos_limpio) > 0:  # Si hay algo
                                    if amigos_limpio[-1] == ",":  # Si termina en coma
                                        amigos_limpio = amigos_limpio[:-1]  # Quitamos la coma
                                
                                if amigos_limpio:  # Si hay algo
                                    amigos = []  # Dividimos por coma
                                    actual = ""
                                    for c in amigos_limpio:
                                        if c == ",":
                                            if actual:
                                                amigos.append(actual)
                                            actual = ""
                                        else:
                                            actual = actual + c
                                    if actual:
                                        amigos.append(actual)
                                    usuarios[nombre_actual]["amigos"] = amigos
            else:  # Si no empieza con *
                # Verificar si empieza y termina con { }
                ultimo_caracter = linea[-1]  # Obtenemos el último carácter
                
                # Si empieza con { y termina con }, son los gustos
                if primer_caracter == "{" and ultimo_caracter == "}":  # Si { y }
                    gustos_str = ""  # Quitamos { y }
                    for i in range(1, len(linea) - 1):
                        gustos_str = gustos_str + linea[i]
                    if gustos_str:  # Si hay contenido
                        gustos = []  # Dividimos por coma
                        actual = ""
                        for c in gustos_str:
                            if c == ",":
                                if actual:
                                    gustos.append(actual.strip())
                                actual = ""
                            else:
                                actual = actual + c
                        if actual:
                            gustos.append(actual.strip())
                        usuarios[nombre_actual]["gustos"] = gustos
                else:  # Si no, es un mensaje
                    if nombre_actual in usuarios:  # Si el usuario actual existe
                        # Agregamos al INICIO para que reciente esté arriba
                        usuarios[nombre_actual]["mensajes"].insert(0, linea)
    
    archivo.close()  # Cerramos el archivo
    print("Datos cargados correctamente")  # Mensaje informativo
    return usuarios  # Devolvemos diccionario con todos los usuarios

def guardar_datos(usuarios):
    """
    Guarda todos los datos en los archivos
    """
    # PASO 1: Guardar nombres y contraseñas en users.txt
    archivo = open("users.txt", "w")  # Abrimos archivo para escribir
    for nombre in usuarios:  # Para cada usuario en el diccionario
        password = usuarios[nombre]["password"]  # Obtenemos su contraseña
        linea = nombre + ";" + password  # Creamos la línea nombre;password
        archivo.write(linea + "\n")  # Escribimos en archivo
    archivo.close()  # Cerramos el archivo
    
    # PASO 2: Guardar información adicional en userData.txt
    archivo = open("userData.txt", "w")  # Abrimos archivo para escribir
    for nombre in usuarios:  # Para cada usuario en el diccionario
        info = usuarios[nombre]  # Obtenemos toda la información del usuario
        
        # Línea 1: Escribir nombre, amigos y solicitudes
        amigos_str = ""  # Unimos lista de amigos con comas
        for i in range(len(info["amigos"])):
            amigos_str = amigos_str + info["amigos"][i]
            if i < len(info["amigos"]) - 1:
                amigos_str = amigos_str + ","
        
        solicitudes_str = ""  # Unimos solicitudes con comas
        for i in range(len(info["solicitudes"])):
            solicitudes_str = solicitudes_str + info["solicitudes"][i]
            if i < len(info["solicitudes"]) - 1:
                solicitudes_str = solicitudes_str + ","
        
        # Armamos línea con formato: *nombre:amigos,<solicitudes>
        if solicitudes_str:  # Si hay solicitudes
            linea_usuario = "*" + nombre + ":" + amigos_str + ",<" + solicitudes_str + ">"
        else:  # Sin solicitudes
            if amigos_str:  # Si hay amigos
                linea_usuario = "*" + nombre + ":" + amigos_str
            else:  # Sin amigos ni solicitudes
                linea_usuario = "*" + nombre + ":"
        
        archivo.write(linea_usuario + "\n")  # Escribimos línea del usuario
        
        # Línea 2: Escribir gustos con formato {gusto1,gusto2}
        gustos_str = ""  # Unimos lista de gustos con comas
        for i in range(len(info["gustos"])):
            gustos_str = gustos_str + info["gustos"][i]
            if i < len(info["gustos"]) - 1:
                gustos_str = gustos_str + ","
        linea_gustos = "{" + gustos_str + "}"  # Armamos la línea con { }
        archivo.write(linea_gustos + "\n")  # Escribimos línea de gustos
        
        # Líneas 3+: Escribir todos los mensajes
        # Los mensajes están en orden: más reciente primero
        for mensaje in info["mensajes"]:  # Para cada mensaje
            archivo.write(mensaje + "\n")  # Escribimos cada mensaje
        
        # Línea en blanco para separar usuarios
        archivo.write("\n")  # Agregamos línea en blanco
    
    archivo.close()  # Cerramos el archivo

def registrar_usuario(nombre, password, usuarios):
    """
    Registra un nuevo usuario en la red social
    Devuelve True si se registró, False si no
    """
    # Validar que el nombre sea solo letras
    es_solo_letras = True
    for caracter in nombre:
        if not ((caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z')):
            es_solo_letras = False
            break
    if not es_solo_letras:  # Si contiene números o caracteres especiales
        return False  # No se puede registrar
    
    # Validar que el usuario no exista ya
    ya_existe = nombre in usuarios  # Verificamos si ya existe
    if ya_existe:  # Si el usuario ya existe
        return False  # No se puede registrar
    
    # Crear nuevo usuario con toda su información
    usuarios[nombre] = {  # Creamos entrada para el nuevo usuario
        "password": password,  # Guardamos su contraseña
        "amigos": [],  # Lista vacía de amigos
        "solicitudes": [],  # Lista vacía de solicitudes
        "gustos": [],  # Lista vacía de gustos
        "mensajes": []  # Lista vacía de mensajes
    }
    
    guardar_datos(usuarios)  # Guardamos los datos en los archivos
    return True  # Registrado exitosamente

def verificar_usuario(nombre, password, usuarios):
    """
    Verifica si el usuario existe y si la contraseña es correcta
    Devuelve True si es correcto, False si no
    """
    # Verificar si el usuario existe
    usuario_existe = nombre in usuarios  # Vemos si está en el diccionario
    if usuario_existe:  # Si el usuario existe
        # Obtener la contraseña guardada
        password_guardada = usuarios[nombre]["password"]  # Obtenemos contraseña
        # Verificar si la contraseña es correcta
        if password_guardada == password:  # Si coincide
            return True  # Contraseña correcta
    # Si no existe o contraseña incorrecta
    return False  # No es correcto

def ver_usuarios(usuarios):
    """
    Muestra todos los usuarios registrados en pantalla
    """
    print("\n=== USUARIOS REGISTRADOS ===")  # Título
    for nombre in usuarios:  # Para cada usuario en el diccionario
        print("- " + nombre)  # Mostramos su nombre

def enviar_solicitud(de_quien, para_quien, usuarios):
    """
    Envía una solicitud de amistad
    Devuelve mensaje de éxito o error explicando qué pasó
    """
    # VALIDACIÓN 1: Verificar que el usuario destino existe
    usuario_existe = para_quien in usuarios  # ¿Existe el usuario?
    if not usuario_existe:  # Si no existe
        return "Error: ese usuario no existe"
    
    # VALIDACIÓN 2: No puede enviarse solicitud a uno mismo
    es_el_mismo = de_quien == para_quien  # ¿Es el mismo usuario?
    if es_el_mismo:  # Si es el mismo
        return "Error: no puedes enviarte solicitud a ti mismo"
    
    # VALIDACIÓN 3: No pueden ser ya amigos
    amigos_de = usuarios[de_quien]["amigos"]  # Obtenemos amigos de quien envía
    ya_son_amigos = para_quien in amigos_de  # ¿Ya son amigos?
    if ya_son_amigos:  # Si ya son amigos
        return "Error: ya son amigos"
    
    # VALIDACIÓN 4: No puede haber solicitud previa del mismo usuario
    solicitudes_para = usuarios[para_quien]["solicitudes"]  # Solicitudes del otro
    ya_envio_solicitud = de_quien in solicitudes_para  # ¿Ya envió?
    if ya_envio_solicitud:  # Si ya envió una
        return "Error: ya enviaste una solicitud a este usuario"
    
    # VALIDACIÓN 5: Si el otro ya te envió solicitud, pídele que acepte
    solicitudes_de = usuarios[de_quien]["solicitudes"]  # Mis solicitudes
    otro_envio_primero = para_quien in solicitudes_de  # ¿Él envió antes?
    if otro_envio_primero:  # Si él ya envió
        return "Error: ese usuario ya te envió solicitud. Acéptala primero"
    
    # Si pasó TODAS las validaciones, enviamos la solicitud
    usuarios[para_quien]["solicitudes"].append(de_quien)  # Agregamos solicitud
    guardar_datos(usuarios)  # Guardamos los cambios en archivos
    return "Solicitud enviada exitosamente"

def ver_solicitudes(nombre, usuarios):
    """
    Obtiene la lista de solicitudes pendientes de un usuario
    Devuelve la lista de solicitudes
    """
    solicitudes_pendientes = usuarios[nombre]["solicitudes"]  # Obtenemos lista
    return solicitudes_pendientes  # Devolvemos

def aceptar_solicitud(nombre, de_quien, usuarios):
    """
    Acepta una solicitud de amistad entre dos usuarios
    Los dos quedan como amigos y se elimina la solicitud
    """
    # Paso 1: Quitar la solicitud de la lista de solicitudes
    usuarios[nombre]["solicitudes"].remove(de_quien)  # Removemos la solicitud
    
    # Paso 2: Agregar como amigos en ambos lados
    usuarios[nombre]["amigos"].append(de_quien)  # Agregamos al otro como amigo
    usuarios[de_quien]["amigos"].append(nombre)  # Agregamos al que aceptó como amigo
    
    # Paso 3: Guardar los cambios en los archivos
    guardar_datos(usuarios)  # Guardamos todo

def ver_mensajes(nombre, usuarios):
    """
    Obtiene la lista de mensajes de un usuario
    Los mensajes están ordenados: más reciente primero
    Devuelve la lista de mensajes
    """
    mensajes_del_usuario = usuarios[nombre]["mensajes"]  # Obtenemos lista
    return mensajes_del_usuario  # Devolvemos

def enviar_mensaje(de_quien, para_quien, texto, usuarios):
    """
    Envía un mensaje de un usuario a otro
    El mensaje incluye fecha, hora y nombre de quien lo envía
    """
    # Paso 1: Obtener fecha y hora actual
    ahora = datetime.datetime.now()  # Obtenemos fecha y hora del sistema
    fecha_hora = ahora.strftime("%d/%m/%Y %H:%M:%S")  # Formateamos: día/mes/año hora:minuto:segundo
    
    # Paso 2: Crear el mensaje con todos los datos
    mensaje = "El " + fecha_hora + " " + de_quien + " escribió: " + texto  # Armamos mensaje
    
    # Paso 3: Agregar el mensaje al inicio de la lista (más reciente va primero)
    usuarios[para_quien]["mensajes"].insert(0, mensaje)  # Insertamos al inicio
    
    # Paso 4: Guardar los cambios en los archivos
    guardar_datos(usuarios)  # Guardamos todo
