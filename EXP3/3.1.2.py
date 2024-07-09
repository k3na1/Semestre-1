# Parte 1
def almacenar_y_mostrar_nombre_largo():
    # Solicitar 3 nombres
    nombres = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    
    # Encontrar el nombre con más caracteres
    nombre_largo = max(nombres, key=len)
    
    # Mostrar el nombre más largo
    print(f"El nombre con más caracteres es: {nombre_largo}")

# Ejecutar la función
almacenar_y_mostrar_nombre_largo()

# Parte 2
def almacenar_y_mostrar_nombres_apellidos():
    # Solicitar 3 nombres
    nombres = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    
    # Solicitar 3 apellidos
    apellidos = []
    for i in range(3):
        apellido = input(f"Ingrese el apellido {i+1}: ")
        apellidos.append(apellido)
    
    # Mostrar nombres y apellidos ordenados
    for nombre, apellido in zip(nombres, apellidos):
        print(f"Nombre: {nombre}, Apellido: {apellido}")

# Ejecutar la función
almacenar_y_mostrar_nombres_apellidos()

# Parte 3
def almacenar_y_eliminar_nombre():
    nombres = []
    continuar = True
    
    while continuar:
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
        
        respuesta = input("¿Desea agregar otro nombre? (sí/no): ")
        if respuesta.lower() != "sí" and respuesta.lower() != "si":
            continuar = False
    
    # Eliminar el nombre con la menor cantidad de caracteres
    if nombres:
        nombre_corto = min(nombres, key=len)
        nombres.remove(nombre_corto)
        print(f"Lista de nombres después de eliminar el más corto: {nombres}")

# Ejecutar la función
almacenar_y_eliminar_nombre()

#Parte 4
usuarios = {}

def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print("Usuario ya existe.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        usuarios[usuario] = contraseña
        print("Usuario registrado correctamente.")

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Error en nombre de usuario o contraseña.")

def eliminar_usuario():
    usuario = input("Ingrese el nombre de usuario que desea eliminar: ")
    if usuario in usuarios:
        contraseña = input("Ingrese la contraseña para confirmar la eliminación: ")
        if usuarios[usuario] == contraseña:
            del usuarios[usuario]
            print("Usuario eliminado correctamente.")
        else:
            print("Contraseña incorrecta. No se pudo eliminar el usuario.")
    else:
        print("Usuario no encontrado.")

def menu_registro():
    while True:
        print("\nMenu de Registro:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú de registro
menu_registro()

#Parte 5
productos = {
    "Leche": 2.5,
    "Pan": 1.0,
    "Huevos": 3.0,
    "Manzanas": 2.0,
    "Arroz": 2.5
}

carro_compras = []

def agregar_producto():
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")
    
    producto = input("Seleccione un producto para agregar al carro: ")
    if producto in productos:
        carro_compras.append(producto)
        print(f"{producto} agregado al carro de compras.")
    else:
        print("Producto no encontrado.")

def ver_canasta():
    print("Productos en el carro de compras:")
    for producto in carro_compras:
        print(producto)

def ver_total():
    total = sum(productos[producto] for producto in carro_compras)
    print(f"Total a pagar: ${total}")

def menu_supermercado():
    while True:
        print("\nMenu de Supermercado:")
        print("1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_canasta()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú del supermercado
menu_supermercado()
