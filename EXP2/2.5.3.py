


def pagoTarjeta(deuda):
    print(f"Tiene una deuda de {deuda}")
    if deuda <= 0:
        print("No tiene deuda que pagar")
        return deuda
    else:
        print("¿Cuanto desea pagar? Escriba 0 si quiere cancelar la operación")
        try:
            deudaPagando = int(input("$ "))
            if deudaPagando >= 1:
                deuda -= deudaPagando
                print(f"Se ha pagado ${deudaPagando} exitosamente")
                return deuda
            elif deudaPagando == 0:
                print("Pago cancelado, volviendo")
                return deuda
            else:
                print("Valor inválido, intente nuevamente")
                return deuda
        except ValueError:
            print("Valor inválido, intente nuevamente")

def comprasTarjeta(deuda):
    total = 0
    flag = True
    try:
        print("¿Cuantos productos desea comprar? Escriba 0 para cancelar la operación")
        productos = int(input("Productos: "))
        if productos == 0:
            print("Compra cancelada, volviendo")
            return deuda
        elif productos >= 1:
            for ind in range(1,productos + 1):
                valor = int(input(f"Valor producto {ind}: "))
                total += valor
            print(f"El total es de {total}. ¿Pagar?")
            while flag == True:
                opc = input("Y/N: ").upper()
                match opc:
                    case "Y":
                        print("Compra realizada con éxito")
                        deudaTotal = deuda + total
                        flag = False
                        return deudaTotal
                    case "N":
                        print("Compra cancelada, volviendo al menú")
                        flag = False
                        return deuda
                    case _:
                        print("Seleccione una opción válida")
    except ValueError:
        print("Valor inválido, intente nuevamente")

deuda = 100000
try:
    while True:
        print("\n     ---- MENÚ TARJETA DE CRÉDITO ----\n1) Pagar deudas\n2) Realizar compras\n3) Salir\n")
        opc = int(input("Opción: "))
        if opc == 1:
            deuda = pagoTarjeta(deuda)
        elif opc == 2:
            deuda = comprasTarjeta(deuda)
        elif opc == 3:
            print("Hasta pronto")
            break
        else:
            print("Seleccione una opción válida")
except:
    print("ERROR. Intente nuevamente")



