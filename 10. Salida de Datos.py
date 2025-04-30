# SALIDA DE DATOS

# Declaramos Nuestras Variables:

nombre = "Lalo"
edad = 23

# Tradicionalmente haríamos algo asi:
print("Hola", nombre, "Tienes", edad, "Años")

# Pero Hay Otra Modo de Imprimir Llamada Format:
print("Hola {} tienes {} años".format(nombre, edad))

'''
La forma de imprimir datos en consola utilizando el método format() se llama "formateo de cadenas".
Es una técnica común en Python para formatear cadenas de texto de manera dinámica,
donde los valores de variables se insertan en la cadena de salida en lugares específicos
indicados por marcadores de posición {}.
El método format() se utiliza para aplicar el formateo de cadenas.
Permite insertar valores de variables en los marcadores de posición
de una cadena y produce una nueva cadena formateada como resultado.
'''

# Hay Otra Forma Mas Moderna:
print(f"Hola {nombre} tienes {edad} años")
# La f"" sirve para indicarle a Python que vamos a utilizar
# la nueva forma de salida de datos por consola.

'''

Esta forma de imprimir datos en consola utilizando f-strings
se llama "formateo de cadenas f" o "f-strings" en Python.
Las f-strings son una característica introducida en Python 3.6
que proporciona una sintaxis más simple y legible para formatear
cadenas de texto que incluyen valores de variables y expresiones de Python.

'''

'''
Cualquier Forma para Imprimir Datos por consola
es Completamente Valida y puedes usar la que más te guste o acomode :)
'''
