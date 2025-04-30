# Capitulo 2 - CONDICIONALES

""" Hacer un Programa que pida 2 Números
y se de cuenta cuál de ellos es par,
o si ambos lo son """

print()  # Salto de Linea

# Le Solicitamos al Usuario 2 Números:
print("PorFavor Digite Unicamente Numeros Enteros (Sin Decimales)")
print()  # Salto de Linea

num1 = int(input("* Digite Un Número: "))
num2 = int(input("* Digite Otro Número: "))

print()  # Salto de Linea

""" Para Saber Si El Número 1 es Par:
Dividimos el Numero 1 Modulo 2 (%) (entre 2) y si
el Residuo es Igual a Cero (==0) Entonces es Par """

# Se Evalua num1 y num2:
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos Numeros Son Pares")
    # Para que se Imprima que Ambos Son Pares
    # Se Debe Cumplir la Sentencia

# Ahora Evaluamos solo si num1 es Par:
# num2 Modulo 2 y si su Residuo es Diferente de Cero (!=0) entonces es Impar.

elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"*** Solamente el {num1} es Par ***")

# Ahora Evaluamos solo si num2 es Par:
# num1 Modulo 2 y si su Residuo es Diferente de Cero (!=0) entonces es Impar.

elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"*** Solamente el {num2} es Par ***")

# Ahora Si Ningun Numero es Par, damos por hecho que Ambos Numeros son Impares:

else:
    print("*** Ambos Numeros son Impares ***")
