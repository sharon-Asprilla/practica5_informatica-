"""
Programa principal de la red social
Aquí comienza el programa y se muestra el menú al usuario
"""
import funciones as fc  # Importamos el archivo funciones.py

def menu_principal(usuarios):
    """
    Menú principal del programa
    Permite registrarse, iniciar sesión o salir
    """
    while True:  # Bucle infinito hasta que salga
        print("\n=== loguin ===")
        print("1. Registrarse")  # Opción 1
        print("2. Iniciar sesión")  # Opción 2
        print("3. Salir")  # Opción 3
        
        opcion = input("Elige una opción: ")  # Pedimos opción
        
        if opcion == "1":  # Si elige 1
            nombre = input("Nombre de usuario: ")  # Pedimos nombre
            password = input("Contraseña: ")  # Pedimos contraseña
            
            ok = fc.registrar_usuario(nombre, password, usuarios)  # Intentamos registrar
            if ok:  # Si se registró bien
                print("¡Registrado exitosamente!")  # Éxito
            else:  # Si no se registró
                print("Error: nombre con letras o usuario existe")  # Error
        
        elif opcion == "2":  # Si elige 2
            nombre = input("Nombre de usuario: ")  # Pedimos nombre
            password = input("Contraseña: ")  # Pedimos contraseña
            
            ok = fc.verificar_usuario(nombre, password, usuarios)  # Verificamos
            if ok:  # Si es correcto
                print("¡Bienvenido " + nombre + "!")  # Saludamos
                menu_usuario(nombre, usuarios)  # Abrimos menú usuario
            else:  # Si no es correcto
                print("Error: usuario o contraseña incorrectos")  # Error
        
        elif opcion == "3":  # Si elige 3
            print("chao")  # Despedida
            break  # Salimos
        
        else:  # Opción inválida
            print("Opción no válida")  # Error

def menu_usuario(nombre, usuarios):
    """
    Menú del usuario después de iniciar sesión
    Aquí puede ver amigos, mensajes, enviar solicitudes, etc.
    """
    while True:  # Bucle hasta cerrar sesión
        # Obtener números de amigos, solicitudes y mensajes
        cantidad_amigos = len(usuarios[nombre]["amigos"])  # Contamos amigos
        cantidad_solicitudes = len(usuarios[nombre]["solicitudes"])  # Contamos solicitudes
        cantidad_mensajes = len(usuarios[nombre]["mensajes"])  # Contamos mensajes
        
        print("\n=== HOLA " + nombre.upper() + " ===")  # Saludo
        print("Amigos: " + str(cantidad_amigos) + " | Solicitudes: " + str(cantidad_solicitudes) + " | Mensajes: " + str(cantidad_mensajes))
        print("1. Ver usuarios")  # Opción 1
        print("2. Enviar solicitud")  # Opción 2
        print("3. Ver solicitudes")  # Opción 3
        print("4. Ver mensajes")  # Opción 4
        print("5. Enviar mensaje")  # Opción 5
        print("6. Cerrar sesión")  # Opción 6
        
        opcion = input("Elige opción: ")  # Pedimos opción
        
        if opcion == "1":  # Ver usuarios registrados
            fc.ver_usuarios(usuarios)  # Mostramos lista de usuarios
        
        elif opcion == "2":  # Enviar solicitud de amistad
            para = input("¿A quién?: ")  # Preguntamos a quién
            resultado = fc.enviar_solicitud(nombre, para, usuarios)  # Enviamos
            print(resultado)  # Mostramos resultado
        
        elif opcion == "3":  # Ver solicitudes de amistad
            solicitudes_lista = fc.ver_solicitudes(nombre, usuarios)  # Obtenemos
            if solicitudes_lista:  # Si hay
                print("\n=== TUS SOLICITUDES ===")  # Título
                for i in range(len(solicitudes_lista)):  # Para cada
                    numero = i + 1  # Número para el usuario
                    usuario = solicitudes_lista[i]  # Nombre usuario
                    print(str(numero) + ". " + usuario)  # Mostramos
                
                opcion2 = input("¿Cuál aceptas? (número): ")  # Preguntamos
                es_numero = True
                for c in opcion2:
                    if not (c >= '0' and c <= '9'):
                        es_numero = False
                        break
                if es_numero:  # Si es número
                    indice = int(opcion2) - 1  # Convertimos a índice
                    if 0 <= indice < len(solicitudes_lista):  # Si es válido
                        quien = solicitudes_lista[indice]  # Obtenemos
                        fc.aceptar_solicitud(nombre, quien, usuarios)  # Aceptamos
                        print("¡Ahora eres amigo de " + quien + "!")  # Confirmamos
            else:  # Si no hay
                print("No tienes solicitudes")  # Mensaje
        
        elif opcion == "4":  # Ver mensajes
            mensajes_lista = fc.ver_mensajes(nombre, usuarios)  # Obtenemos
            if mensajes_lista:  # Si hay
                print("\n=== TUS MENSAJES ===")  # Título
                print("(Del más reciente al más antiguo)")  # Aclaración
                for msg in mensajes_lista:  # Para cada mensaje
                    print(msg)  # Mostramos
            else:  # Si no hay
                print("No tienes mensajes")  # Mensaje
        
        elif opcion == "5":  # Enviar mensaje a un amigo
            amigos_lista = usuarios[nombre]["amigos"]  # Obtenemos amigos
            if amigos_lista:  # Si hay amigos
                print("Tus amigos: " + str(amigos_lista))  # Mostramos
                para = input("¿A quién?: ")  # Preguntamos
                
                if para in amigos_lista:  # Si es amigo
                    texto = input("Mensaje: ")  # Pedimos mensaje
                    fc.enviar_mensaje(nombre, para, texto, usuarios)  # Enviamos
                    print("Enviado")  # Confirmamos
                else:  # Si no es amigo
                    print(" no es tu amigo")  # Error
            else:  # Sin amigos
                print("No tienes amigos")  # Mensaje
        
        elif opcion == "6":  # Cerrar sesión
            print("sesion cerrada")  # Mensaje
            break  # Salimos
        
        else:  # Opción inválida
            print("Opción no válida")  # Error

def main():
    """
    Función principal del programa
    Aquí comienza todo
    """
    usuarios = fc.cargar_datos()  # Cargamos datos de los archivos
    menu_principal(usuarios)  # Mostramos el menú principal

# Ejecutar el programa
main()  # Llamamos a main para iniciar