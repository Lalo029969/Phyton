# Ejercicio 2

'''
Determinar la Solución Lógica de
la siguiente Operación:

((3+5x8)<3 and ((-6 Tercios x4)+2<2)) or (a>b)

'''


# Variables
''' Se Solicita al Usuario el Valor de A y B'''

print() #Salto de Linea

a = float(input("Digite el Valor de a: "))
b = float(input("Digite el Valor de b: "))

print() #Salto de Linea

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print (f"El Resultado Es: {resultado}")


'''
Dependiendo los Valores Ingresados por el Usuario
para las Variables A y B, los operandos
daran como resultado True o False.

Por Ejemplo:
Si le Asignamos los siguientes Valores
A = 10
B = 5

Se Va a Evaluar de la Siguiente Manera:

((3+5x8)<3 and ((-6/3x4)+2<2)) or (a>b)
((3+5x8)<3 and ((-6/3x4)+2<2)) or (10>5)
(5x8=40+3=43 and (-6/3=-2x4=-8+2=10) or True
(43<3? False and -10<2? True or True
(False and True) or True
False or True
True

Para el Operando or Basta con que uno sea True
Para que todo el Resultado sea True.

'''






