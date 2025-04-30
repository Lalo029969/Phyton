# CAJERO AUTOMÁTICO

"""
Menú de Opciones

1. Depositar Dinero a la Cuenta
2. Retirar Dinero de la Cuenta
3. Consultar Saldo
4. Salir
"""

# Inicializamos el Saldo en 10
saldo = 0

print() # Salto de Linea
print("Bienvenido(a) al Cajero Automático")
print() # Salto de Linea
print("\t*** MENÚ DE OPCIONES ***")
print("1. Depositar Dinero a la Cuenta")
print("2. Retirar Dinero de la Cuenta")
print("3. Consultar Saldo")
print("4. Salir")

print()  # Salto de Linea

opcion = int(input("Digite la Opción que Desea Realizar: "))

print()  # Salto de Linea


if opcion == 1:
    deposito = float(input("Ingrese la Cantidad que Desea Depositar: "))
    saldo = saldo + deposito
    print(f"Su Saldo Disponible Ahora Es De: {saldo}")

    

elif opcion == 2:
    retiro = float(input("Ingrese la Cantidad que Desea Retirar: "))
    if retiro > saldo:
        print("No Tiene Dinero Suficiente")
    else:
        saldo = saldo - retiro
        print("Retiro Exitoso")
        print(f"Ahora Su Saldo Disponible Es De: {saldo}")



elif opcion == 3:
    print(f"Su Saldo Disponible Es De: {saldo}")

elif opcion == 4:
    print("Gracias por Utilizar el Cajero Automático")

else:
    print("ERROR (Opción Invalida)")
