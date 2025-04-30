# ENTRADA DE DATOS

# Le pediremos al usuario los Datos:

nombre = input("Digita Tu Nombre: ")
# Input sirve para almacenar datos de Tipo Cadena (str: string)
print () # Salto de Linea

'''
En Python, los valores de cadena (strings) son secuencias de caracteres encerrados entre comillas simples (')
o comillas dobles ("). Los caracteres pueden ser letras, números, símbolos o incluso espacios en blanco.

Algunos ejemplos de valores de cadena válidos en Python son:

cadena1 = 'Hola Mundo'
cadena2 = "Python es Genial"
cadena3 = '12345'
cadena4 = "¡@#$%^&*()"
cadena5 = ' '
En estos ejemplos, cadena1, cadena2, cadena3, cadena4 y cadena5
son variables que contienen valores de cadena diferentes.
Puedes utilizar estas cadenas en operaciones de cadena,
como concatenación, indexación, corte, entre otros.
Las cadenas son inmutables en Python, lo que significa que
una vez que se crean, no se pueden modificar.
Sin embargo, puedes crear nuevas cadenas basadas
en las originales utilizando
diferentes métodos de manipulación de cadenas.

input() es una función integrada en Python
que se utiliza para recibir entrada del usuario
a través de la consola.
Cuando se llama a la función input(),
el programa se detiene y espera a que el usuario ingrese algún texto.
Después de que el usuario ingresa el texto y presiona la tecla "Enter",
el programa continúa su ejecución y el texto ingresado por el usuario
se devuelve como una cadena de caracteres.
'''

print(f"Hola {nombre}")
print () # Salto de Linea

# Para Guardar Numeros Enteros en la Variable, se hace de la siguiente manera:

edad = int(input("Ahora Digita un Número Entero: "))
# Debemos colocar int antes del input
# Para Indicarle a que se van a capturar datos de tipo entero o numericos.

print () # Salto de Linea
print(f"El Número que Digitaste Es: {edad}")
print () # Salto de Linea

# Para Guardar Numeros con Punto Decimal en la Variable, se hace de la siguiente manera:

edad = float(input("Ahora Digita un Número con Punto Decimal: "))
# Debemos colocar float antes del input
# Para Indicarle a que se van a capturar datos numericos con punto decimal.

print () # Salto de Linea
print (f"El Número que Digitaste Es: {edad}")
print () # Salto de Linea

# Ahora Agregamos un Mensaje de Salida al Usuario al finalizar el Programa:
print(f" *** Gracias por Utilizar el Programa de Entrada de Datos *** ")
print(f"     ¡Que Tengas un Excelente Dia {nombre}!")
