# FUNCIONES INTEGRADAS

# Convierte a la Cadena en un Valor de Tipo Entero (int)
x = int ("10")
# Imprimir Valor
print (x)


# Convierte a la Cadena en un Valor de Tipo Flotante (float)
x = float ("10.58")
# Imprimir Valor
print (x)


# Convierte un Valor Numerico Entero (int) en una Cadena (str)
x = str (13)
# Imprimir Valor
print (x)

# Convierte un Valor Flotante (float) en una Cadena (str)
x = str (53.71)
# Imprimir Valor
print (x)

# Convierte un Valor Entero (int) a un Valor Binario (bin)
x = bin (20)
# Imprimir Valor
print (x)

# Convierte un Valor Entero (int) a un Valor Hexadecimal (hex)
x = hex (20)
# Imprimir Valor
print (x)

# Convierte un Valor Binario (bin) a un Valor Entero (int)
x = int ("0b10110110",2)
# ,2 se Usa para Indicarle la Base de Conversion del Numero
# Imprimir Valor
print (x)


# Convierte un Valor Hexadecimal (hex) a un Valor Entero (int)
x = int ("0xa",16)
# ,16 se Usa para Indicarle la Base de Conversion Hexadecimal que es = 16
print (x)


# Sacar el Valor Absoluto de un Numero
'''El Valor Absoluto Es:
 La Distancia del Numero hacia el Cero pero siempre en Positivo'''

x = abs(-3) # Su Distancia hacia el Cero es: -2, -1, 0.
print (x) # Por lo Tanto va a Imprimir 3

x = abs(5) # Su Distancia hacia el Cero es: 4, 3, 2, 1, 0.
print (x) # Por lo Tanto va a Imprimir 5

x = abs(0) # Su Distancia hacia el Cero es: 0.
print (x) # Por lo Tanto va a Imprimir 0.


'''
La Función Round:
Redondear un Numero Decimal a la Alza o a la Baja
dependiento la terminacion decimal que Tenga
'''

x = round(5.6) # .6 Lo Redondea Hacia Arriba
print (x) # Por lo Tanto va a imprimir 6

x = round(5.5) # .5 Lo Redondea Hacia Arriba
print (x) # Por lo Tanto va a imprimir 6

x = round(5.4) # .4 Lo Redondea Hacia Abajo
print (x) # Por lo Tanto va a imprimir 5


'''
La Función Len:
Sirve para contar el numero de caracteres
almacenados en una Cadena
'''

x = len("Dificultad") # Tiene 10 Letras
print (x) # Por lo Tanto va a Imprimir el Numero 10
