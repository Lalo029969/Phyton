""" Ejercicio 3:
Hacer un Programa que Pida un Carácter e Indique
si es una Vocal o No
"""

print() # Salto de Linea

print(" *** PROGRAMA PARA VALIDAR SI LA LETRA INGRESADA")
print("     POR EL USUARIO ES UNA VOCAL O NO *** ")

print() # Salto de Linea

letra= input("Digite una Letra: ").lower()

"""
.lower() sirve para Transformar una Letra Mayuscula
en una Minuscula, de esta manera si el usuario
ingresa cualquier letra en Mayuscula, nos va a respetar
nuestra siguiente condición: """

if letra=='a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print()  # Salto de Linea
    print (f"La Letra {letra} SI es una Vocal")

else:
    print()  # Salto de Linea
    print(f"{letra} NO es una Vocal")




