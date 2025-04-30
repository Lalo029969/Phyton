# CONDICIONALES COMBINADOS

""" Vamos a Validar si el Usuario es Mayor de Edad """

# Le Pedimos al Usuario su Edad:
edad = int(input("Ingrese Su Edad: "))

# Si la Edad es Mayor a 0 y Menor a 100:
""" Otra Forma mas Simple de Hacer lo que esta a Continuacion Seria Asi: if 0<edad<100:
                            Y es Exactamente lo Mismo pero Utilizando Operadores Relacionales Combinados.
                            Compara Si Edad es Mayor a 0 y Menor a 100.
                            Y Para que el Condicional se cumpla deben cumplirse ambas Comparaciones. """

if edad>0 and edad<100:
#if 0<edad<100:
    print ("El Valor Ingresado es una Edad Lógica")
    # Se Considera que es un Rango de Edad Adecuado

# Esto es una Condicion Combinada:
    # Un "if" dentro de otro "if"

    if edad>=18:
       print("Usted Es Mayor de Edad")

# Adicionalmente Coloque un Else para que Tenga mas Sentido el Programa:
    else:
        print("Pero Usted NO Es Mayor de Edad")

        """ En Donde El Usuario puede Ingresar Numeros del 0 al 17
        Y Son Valores Logicos pero No es Mayor o Igual a 18
        Para que se Considere Mayor de Edad y por lo Tanto Se Imprime
        El Valor Ingresado es una Edad Lógica
        Pero Usted NO Es Mayor de Edad"""

# Si Ninguna de las Condiciones Anteriores Se Cumple Entonces:

else:
    print("Esa Edad No Existe")

    """ Casos Como que el Usuario Ingrese
    Valores Ilogicos Como Menores a Cero (-1,-2,-3...)
    O Valores Exagerados como (200, 500, o 10000 Años)
    Evidentemente Una Persona
    No puede Tener -1 Año, Ni Mucho Menos Puede Tener 1000 Años
    """

"""
NOTA IMPORTANTE:
*En Phyton No Existen los Condicionales Multiples*
Como Por Ejemplo: El Famoso "Switch"
Pero Podemos Simular algo parecido
con la ayuda de los Rangos, los Operandos (AND, OR, NOT), los Operadore Logicos Combinados,
el if, elif, else, Los Condicionales Anidados.
"""