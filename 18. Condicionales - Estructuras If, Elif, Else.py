# Estructuras Condicionales

""" Son de las Estructuras de Control
mas Importantes en toda la Programación.

Estas sentencias nos sirven para comparar
2 Valores, y esta comparacion me va a dar
un Valor Lógico (Verdadero o Falso).

Si una Determinada Condición se cumple
se van a ejecutar un determinado número de acciones.

Puede que se Ejecute otro numero de acciones
o Puede que NO se Ejecute Nada. """

print() # Salto de Linea

# Le Pedimos al Usuario que nos Digite un Número:

numero = float(input("Digite un Numero: "))
print() # Salto de Linea


# SENTENCIA "if"
# Se Traduce Como: "si".
# Se utiliza para ejecutar un bloque de código si una condición es verdadera.


# Si Número es Mayor a Cero:
if numero > 0:  # Colocamos (:) para Indicarle a la Sentencia que ahi Termina la Condicion que queremos Evaluar.
    print("*** El Numero que Digitó es Positivo ***")

    ''' Por lo Regular en Otros Lenguajes de Programacion se abren una llaves {}
    para Indicarle a la Sentencia el Contenido que va a Evaluar si se cumple la Condición
    pero en Phyton no se ponen esas Llaves {}
    simplemente se coloca un Espacio en la siguiente línea
    este pequeño espacio se le conoce como
    Identación o Sangría. '''

# SENTENCIA "elif" (Abreviatura de else con if)
# Se Traduce Como: "si no, si" o "en caso contrario, si".
# Se Utiliza para agregar una condición adicional que se evalúa si la condición del if es falsa o no se cumple.


elif numero == 0:  # Usamos (==) Para Comparar Si el Numero es Igual a Cero
    # Del Mismo Modo Colocamos (:) para Indicarle a la Sentencia que ahi Termina la Condicion que queremos Evaluar.
    print("*** El Numero que Digitó es Cero ***")

    ''' Como la Condicion Anterior dice que Si el Numero que el Usuario Ingrese es Mayor a Cero,
    Va a Imprimir que el Numero que Ingresó es Positivo, pero si el Usuario Ingresa exactamente el Numero Cero
    Entonces el Programa va a Saltar a la Sentencia "elif" y Va a Imprimir que
    El Numero que Ingresó es Cero '''


# SENTENCIA "else"
# Se Traduce Como: "si no" o "sino".
# Se Utiliza para ejecutar un bloque de código si la condición del if es falsa.

else:
    print("*** El Numero que Digitó es Negativo ***")
    ''' En Este Caso si el Usuario Ingresa un Numero Menor a Cero (-1,-2,-3...)
    Entonces va a Imprimir que el Numero que Digitó es Negativo.
    '''

# Mas Detallado:
'''
if, else y elif son palabras clave utilizadas en Python
para controlar el flujo de ejecución del programa basado
en ciertas condiciones. Se pueden clasificar como
estructuras de control de flujo o construcciones condicionales.

if: Se utiliza para evaluar una expresión booleana
y ejecutar un bloque de código si la expresión es verdadera.

else: Se utiliza en conjunto con if para ejecutar un bloque de código alternativo
si la expresión condicional del if es falsa.

elif (abreviatura de "else if"): Se utiliza para agregar múltiples condiciones a una estructura if.
Si la condición del if es falsa, elif permite evaluar otra condición y ejecutar
un bloque de código asociado si esa condición es verdadera.

Aunque estas palabras clave se utilizan en la formulación de condiciones,
son estructuras de control de flujo que permiten tomar decisiones basadas en esas condiciones.


* ¿En que orden se deben escribir en el codigo las sentencias si solo uso if y else?

En Python, cuando se utiliza solo if y else, las sentencias se escriben de la siguiente manera:

if condicion:
    # bloque de código si la condición es verdadera
else:
    # bloque de código si la condición es falsa


Aquí, el bloque de código bajo if se ejecuta si la condición especificada es verdadera.
Si la condición es falsa, se ejecuta el bloque de código bajo else.

* Es importante notar que el bloque else es opcional y se ejecuta solo si no se cumple la condición del if.


* ¿En que orden se deben escribir en el codigo las sentencias si uso las 3 Sentencias?

Cuando se utilizan las tres sentencias if, elif y else en Python, el orden generalmente se sigue de la siguiente manera:

if condicion1:
    # bloque de código si condicion1 es verdadera
elif condicion2:
    # bloque de código si condicion2 es verdadera
elif condicion3:
    # bloque de código si condicion3 es verdadera
else:
    # bloque de código si ninguna de las condiciones anteriores es verdadera
    
En este caso, el programa evalúa cada condición en orden.
Si alguna de las condiciones if o elif se evalúa como verdadera,
se ejecuta el bloque de código correspondiente y el resto de las sentencias elif y else se omiten.

Si ninguna de las condiciones anteriores es verdadera, se ejecuta el bloque de código bajo else.

Es importante destacar que else es opcional y puede omitirse
si no se necesita un bloque de código que se ejecute cuando
ninguna de las condiciones anteriores sea verdadera.

'''

# SIGNIFICADO EN ESPAÑOL

'''
if se traduce como "si".
else se traduce como "si no" o "sino".
elif se traduce como "si no, si" o "en caso contrario, si".

Estas traducciones reflejan el propósito de cada una de estas sentencias en Python.
Por ejemplo:
if se utiliza para ejecutar un bloque de código si una condición es verdadera,
else se utiliza para ejecutar un bloque de código si la condición del if es falsa,
elif se utiliza para agregar una condición adicional que se evalúa si la condición del if es falsa.

'''