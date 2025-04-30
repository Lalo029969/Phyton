# Operación Aritmetica

# Variables:
a = float (input("Digite el Valor de a: "))
b = float (input("Digite el Valor de b: "))
c = float (input("Digite el Valor de c: "))

print () # Salto de Linea

resultado = (a**3 * (b ** 2 - 2*a*c))/(2*b)

print (f"El Resultado Es: {resultado}")

print () # Salto de Linea


'''
*Ejercicio 2 de Prueba*
Determinar la Solución Lógica de la Siguiente Operación:
((3+5x8)<3 and ((-6 x 4)+2<2)) or (a>b)
                  -
                  3
'''

# SOLUCIÓN

a = 3
b = 5
c = 8
d = -6/3
e = 4
f = 2

resultado = float ((a+b*c)<a) and ((d*e)+f<f) or (a>b)


print () # Salto de Linea
print (f"Resultado del Ejercicio 2: {resultado}") # False






