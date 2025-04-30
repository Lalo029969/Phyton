# Operadores Aritmeticos

'''

Suma: +

Resta: -

Multiplicación: *

Division: /
Te da el Resultado con Decimales

Division Redondeado a la Baja: //

Modulo: %
Te Da el Residuo de una Division
Ejemplo 10/3 = Sobra 1

Exponenciación: **
Un Numero Elevado a una Potencia
Ejemplo 3 a la 3 = 27
Se escribe 3**3


'''


#Variable que se llama Resultado
resultado = 10 + 5
# Guardo 2 Valores de Suma en la Variable

print ("\n")
print ("El Resultado de la Suma Es: ", resultado)

#Imprimo el Resultado de la Suma, Pero eso no tiene mucho sentido

#Mejor Creamos 2 Variables y le Asignamos un Valor a Cada Una

num1 = 10
num2 = 5

#Imprimo la suma de los Valores Almacenados en Mis Variables
print ("El Resultado de la Suma Es: ", num1+num2)


#Ejemplo de Operacion con Modulo

num3 = 10
num4 = 3

print ("El Sobrante de Dividir 10/3 Es: ", num3 % num4)

#Ejemplo de Operacion con Exponenciacion
num5 = 2
num6 = 5

print ("El Resultado de 2 ELevado a la Quinta Potencia Es: ", num5 ** num6)

# El Numero 2 es Elevado a la Quinta Potencia


'''

En Phyton se le da la Prioridad a los Operadores Aritmeticos
Igual que en Matematicas

1. Se Evaluan los Parentesis () de Adentro hacia Afuera
2. La Exponenciacion **
3. Multiplicacion, Division y Modulo *, /, %
4. Suma y Resta +, -

'''

# Ejemplo 1

resultado = 3**3 * (13/5 - (2*4))

print ("El Resultado de la Operación Aritmetica Es: " ,resultado)

'''

1. Resuelve los Parentesis Mas Internos
que son 2x4 = 8

2. Resuelve los Parentesis Restantes
La Division de 13/5
Y despues la Resta 13/5 - 8 = 5.4

3. Resuelve la Potencia
3 al Cubo = 27

4. Resuelve
27 x 5.4 = -145.8

'''


