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

suma = numero1 + numero2
print()  # Salto de Línea
print(f"La Suma Es: {suma}")

resta = numero1 - numero2
print()  # Salto de Línea
print(f"La Resta Es: {resta}")

multiplicacion = numero1 * numero2
print()  # Salto de Línea
print(f"La Multiplicación o el Producto Es: {multiplicacion}")

division = numero1 / numero2
print()  # Salto de Línea
print(f"La División Es: {division:.2f}")
