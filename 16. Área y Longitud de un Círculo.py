'''
Ejercicio #4:
Hacer un programa en donde el usuario ingrese el radio
de un circulo y obtenga como resultado su área
y la longitud de la circunferencia.
'''

# Esto es un Módulo Integrado en Phyton

import math # Importamos este modulo porque es el que contiene integrado el valor de Pi (3.1416...)

print() # Salto de Línea

# Solicitamos al Usuario el Valor del Radio
radio = float(input("Digite el Valor del Radio del Circulo: "))
# Por lo Regular este Valor es de Tipo Flotante

print() # Salto de Línea

# Calculamos el Área
area = math.pi * radio**2
# Calculamos la Longitud
longitud = 2*math.pi * radio

# Imprimimos el Resultado del Área
print(f"El Área del Circulo Es: {area:.2f}")

# Imprimimos el Resultado de la Longitud
print(f"La Longitud del Circulo Es: {longitud:.2f}")


'''
Utilizamos (:.2f) para Obtener Solo 2 Decimales
Al Momento de Imprimir los Resultados
'''
