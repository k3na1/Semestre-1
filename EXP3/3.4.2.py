#Ejercicio 1

# Función para sumar dos números enteros
def sumar(a, b):
    return a + b

# Función para restar dos números enteros
def restar(a, b):
    return a - b

# Función para multiplicar dos números enteros
def multiplicar(a, b):
    return a * b

# Función para dividir dos números enteros, con validación de división por cero
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

# Función principal para ejecutar la calculadora
def calculadora():
    # Ingreso de números y operación
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        
        opcion = int(input("Seleccione la operación (1/2/3/4): "))
        
        if opcion == 1:
            resultado = sumar(num1, num2)
            print(f"\nResultado de la suma: {resultado}")
        elif opcion == 2:
            resultado = restar(num1, num2)
            print(f"\nResultado de la resta: {resultado}")
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
            print(f"\nResultado de la multiplicación: {resultado}")
        elif opcion == 4:
            resultado = dividir(num1, num2)
            print(f"\nResultado de la división: {resultado}")
        else:
            print("Opción no válida")
    
    except ValueError:
        print("Error: Ingrese solo números enteros")

# Ejecutar la calculadora
calculadora()


#Ejercicio 2

# Función para validar y obtener un número entero
def obtener_numero_entero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Ingrese solo números enteros")

# Función para validar y obtener un número decimal (float)
def obtener_numero_decimal(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error: Ingrese un número válido")

# Función principal para ejecutar la calculadora con validaciones
def calculadora_con_validacion():
    # Ingreso de números y operación
    try:
        num1 = obtener_numero_decimal("Ingrese el primer número: ")
        num2 = obtener_numero_decimal("Ingrese el segundo número: ")
        
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        
        opcion = int(input("Seleccione la operación (1/2/3/4): "))
        
        if opcion == 1:
            resultado = sumar(num1, num2)
            print(f"\nResultado de la suma: {resultado}")
        elif opcion == 2:
            resultado = restar(num1, num2)
            print(f"\nResultado de la resta: {resultado}")
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
            print(f"\nResultado de la multiplicación: {resultado}")
        elif opcion == 4:
            resultado = dividir(num1, num2)
            print(f"\nResultado de la división: {resultado}")
        else:
            print("Opción no válida")
    
    except ValueError:
        print("Error: Ingrese solo números válidos")

# Ejecutar la calculadora con validación
calculadora_con_validacion()
