# Capitulo 2 - CONDICIONALES

""" Ejercicio 2
* Hacer un Programa que Pida 3 Numeros
y Determine cuál es el Mayor """

print()  # Salto de Linea

# Le Solicitamos al Usuario 3 Números:
print("PorFavor Digite Unicamente Numeros Enteros (Sin Decimales)")
print()  # Salto de Linea

num1 = int(input("Digite el Primer Número: "))
num2 = int(input("Digite el Segundo Número: "))
num3 = int(input("Digite el Tercer Número: "))

print()  # Salto de Linea

# Evaluamos para cuando el Primer Numero es el Mayor:

if num1 >= num2 and num1 >= num3:
    print(f"El Numero {num1} es el Mayor")

# Evaluamos para cuando el Segundo Numero es el Mayor:

elif num2 >= num1 and num2 >= num3:
    print(f"El Numero {num2} es el Mayor")

# Evaluamos para cuando el Tercer Numero es el Mayor:

elif num3 >= num1 and num3 >= num2:
    print(f"El Numero {num3} es el Mayor")

# Si Ninguna de las Sentencias Anteriores se Cumple
# Entonces Damos por Hecho que Todos son Iguales:

else:
    print("Todos Los Numeros son Iguales")
