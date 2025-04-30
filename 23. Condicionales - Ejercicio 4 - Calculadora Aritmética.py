# CALCULADORA ARITMÉTICA

"""
S, s - Suma
R, r - Resta
P, p, M, m - Producto o Multiplicación
D, d - División
"""

# Le Pedimos al Usuario 2 Números:
print()  # Salto de Línea
numero1 = float(input("Digite un Numero: "))
print()  # Salto de Línea
numero2 = float(input("Digite otro Numero: "))
print()  # Salto de Línea
operacion = input("Digite la Operación que Desea Realizar: ").upper().lower()

""" El método .upper() se utiliza para convertir una cadena de texto en mayúsculas.
Este método retorna una nueva cadena que consiste en
todos los caracteres convertidos a mayúsculas. """

if operacion == 'suma':
    suma = numero1 + numero2
    print()  # Salto de Línea
    print(f"La Suma Es: {suma}")

elif operacion == 'resta':
    resta = numero1 - numero2
    print()  # Salto de Línea
    print(f"La Resta Es: {resta}")


elif operacion == 'multiplicacion' or operacion=='producto':
    multiplicacion = numero1 * numero2
    print()  # Salto de Línea
    print(f"La Multiplicación o el Producto Es: {multiplicacion}")

elif operacion == 'division':
    division = numero1 / numero2
    print()  # Salto de Línea
    print(f"La División Es: {division:.2f}")

else:
    print("Operación No Válida, Reintente Nuevamente")
