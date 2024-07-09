import re

# Variables de usuarios y contraseñas
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

def menuPrincipal():
    while True:
        print("*********** Menú Principal ************")
        print("1) Iniciar sesión")
        print("2) Registrar usuario")
        print("3) Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                iniciarSesion()
            elif opcion == 2:
                registrarUsuario()
            elif opcion == 3:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def registrarUsuario():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    for i in range(1, 4):
        if globals()[f"usuario{i}"] is None:
            username = input(f"Ingrese el nombre de usuario {i}: ")
            password = input(f"Ingrese la contraseña para {username}: ")
            globals()[f"usuario{i}"] = username
            globals()[f"contrasena{i}"] = password
            print("Usuario registrado exitosamente.")
            return
    print("No se pueden registrar más usuarios.")

def iniciarSesion():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    if usuario1 is None and usuario2 is None and usuario3 is None:
        print("No hay usuarios registrados. Por favor, registre un usuario primero.")
        return
    
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if (username == usuario1 and password == contrasena1) or \
       (username == usuario2 and password == contrasena2) or \
       (username == usuario3 and password == contrasena3):
        menuUsuario()
    else:
        print("Usuario o contraseña incorrectos.")

def menuUsuario():
    while True:
        print("*********** Menú Usuario ************")
        print("1) Realizar llamada")
        print("2) Enviar correo electrónico")
        print("3) Cerrar sesión")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                realizarLlamada()
            elif opcion == 2:
                enviarCorreo()
            elif opcion == 3:
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def realizarLlamada():
    while True:
        numero = input("Ingrese el número de celular (9 dígitos, debe comenzar con 9): ")
        if re.match(r'^9\d{8}$', numero):
            print(f"Llamando al número {numero}...")
            break
        else:
            print("Número inválido. Intente nuevamente.")

def enviarCorreo():
    correo = ""
    while "@" not in correo:
        correo = input("Ingrese el correo electrónico: ")
        if "@" not in correo:
            print("Correo inválido. Debe contener '@'. Intente nuevamente.")
    mensaje = input("Ingrese el mensaje a enviar: ")
    print(f"Correo enviado a {correo} con el mensaje: {mensaje}")

# Iniciar el programa
menuPrincipal()
