#Actividad 1

patio = True
pasillo = True
sala = True
jardin = True

print(f"1) Encender/Apagar luces Patio (Alternar)")
print(f"2) Encender/Apagar luces Pasillo (Alternar)")
print(f"3) Encender/Apagar luces Sala (Alternar)")
print(f"4) Encender/Apagar luces Jardín (Alternar)")
print(f"5) Encender todas las luces (Alternar)")
print(f"6) Apagar todas las luces (Alternar)")
print(f"7) Salir")

while True:
    try:
        opc = int(input("Opción: "))
        if opc == 1:
            if patio == True:
                patio = False
                print("Luz patio apagada")
            else:
                patio = True
                print("Luz patio prendida")        
        elif opc == 2:
            if pasillo == True:
                pasillo = False
                print("Luz pasillo apagada")
            else:
                pasillo = True
                print("Luz pasillo prendida")  
        elif opc == 3:
            if sala == True:
                sala = False
                print("Luz sala apagada")
            else:
                sala = True
                print("Luz sala prendida")  
        elif opc == 4:
            if jardin == True:
                jardin = False
                print("Luz jardin apagada")
            else:
                jardin = True
                print("Luz jardin prendida") 
        elif opc == 5:
            patio = True
            pasillo = True
            sala = True
            jardin = True
            print("Todas las luces prendidas")
        elif opc == 6:
            patio = False
            pasillo = False
            sala = False
            jardin = False
            print("Todas las luces apagadas")
        elif opc == 7:
            print("Hasta luego")
            break
        else:
            print("Seleccione una opción válida")
    except:
        print("ERROR")

import random
import string

# Actividad 2

def tarjetaCredito(pago):
    numTarjeta = input("Ingrese número de su tarjeta: ")
    nomTarjeta = input("Nombre del titular: ")
    mesTarjeta = input("Mes de vencimiento: ")
    anoTarjeta = input("Año vencimiento: ")
    print("\n********Detalle de compra********")
    print(f"Costo compra: {pago}\nNumero de tarjeta: {numTarjeta}\nNombre titular: {nomTarjeta.capitalize()}\nMes y año: {mesTarjeta}/{anoTarjeta}")

def paypal(pago):
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    print("\n********Detalle de compra********")
    print(f"Costo compra: {pago}\n Usuario: {user}")

def transferencia(pago):
    refRandom = random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper())
    print("Numero de cuenta: 213211234")
    print(f"Código de referencia: {refRandom}")

print("")
opcion = 0
pago = 100000
while True:
    print("***************Menu*******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    print("")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except:
        opcion = 0
    if opcion == 1:
        tarjetaCredito(pago)
    elif opcion == 2:
        paypal(pago)
    elif opcion == 3:
        transferencia(pago)
    elif opcion == 4:
        print("Pago cancelado")
    elif opcion == 5:
        print("Hasta pronto...")
        break
    else:
        print("Opción no válida")
    print("")
print("")
print ("Muchas gracias por su compra")
print("")


# Actividad 3

print("")
print("Calculadora geométrica")
print("")

while True:
    print("***********Menú************")
    print("1. Calcular Perímetro")
    print("2. Calcular Área")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    print("")

    if opcion == 1:
        print("Calcular Perímetro")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver al menú principal")
        opcion2 = int(input("Elija una opción: "))
        print("")

        if opcion2 == 1:
            radio = int(input("Ingrese radio del círculo: "))
            perimetro = 2 * 3.14 * radio
            print("Perímetro del círculo: ", perimetro)
            print("")
        elif opcion2 == 2:
            altura = int(input("Ingrese altura del rectángulo: "))
            ancho = int(input("Ingrese ancho del rectángulo: "))
            perimetro = 2 * (altura + ancho)
            print("Perímetro del rectángulo: ", perimetro)
            print("")
        elif opcion2 == 3:
            lado = int(input("Ingrese lado del cuadrado: "))
            perimetro = 4 * lado
            print("Perímetro del cuadrado: ", perimetro)
            print("")
        elif opcion2 == 4:
            continue
        else:
            print("Elección inválida.")
            print("")

    elif opcion == 2:
        print("Calcular Área")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver al menú principal")
        opcion3 = int(input("Elija una opción: "))
        print("")

        if opcion3 == 1:
            radio = int(input("Ingrese radio del círculo: "))
            area = 3.14 * radio * radio
            print("Área del círculo: ", area)
            print("")
        elif opcion3 == 2:
            altura = int(input("Ingrese altura del rectángulo: "))
            ancho = int(input("Ingrese ancho del rectángulo: "))
            area = altura * ancho
            print("Área del rectángulo: ", area)
            print("")
        elif opcion3 == 3:
            lado = int(input("Ingrese lado del cuadrado: "))
            area = lado * lado
            print("Área del cuadrado: ", area)
            print("")
        elif opcion3 == 4:
            continue
        else:
            print("Elección inválida.")
            print("")
    
    elif opcion == 3:
        break
    
    else:
        print("Elección inválida.")
        print("")

# Actividad 5

def calcularPisos(totalLadrillos):
    pisos = 0
    ladrillosUsados = 0

    while True:
        pisos += 1
        ladrillosNecesarios = pisos
        
        if ladrillosUsados + ladrillosNecesarios <= totalLadrillos:
            ladrillosUsados += ladrillosNecesarios
        else:
            break
    
    return pisos - 1

# Ejemplo de uso:
totalLadrillos = int(input("Ingrese la cantidad total de ladrillos: "))
pisos = calcularPisos(totalLadrillos)
print("La cantidad de pisos que tendrá la pirámide es:", pisos)


# Actividad 4

import time

contador = 0
flag = True
while flag == True:
    if contador == 50:
        flag = False

    espacios = ""
    linea = "*"
    
    for i in range(11):
        print(linea)
        espacios += " "
        linea = espacios + linea
        time.sleep(0.05)
    
    for i in range(14):
        print(linea)
        linea = linea[i:]
        time.sleep(0.05)
    
    linea = "*"
    espacio = " "
    for i in range(22):
        linea += " *"
        espacio += " "
        print(linea)
        time.sleep(0.05)
    
    espacio += "*"
    for i in range(14):
        print(espacio)
        time.sleep(0.05)
    
    print(linea)
    contador += 1




