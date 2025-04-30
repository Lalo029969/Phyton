# OPERADORES LÓGICOS

"""
* Permiten Construir Expresiones Lógicas, y se obtiene
como resultado un valor Booleano.

1. AND (Conjunción) - and (Multiplicación Lógica)
2. OR (Disyunción) - or (Suma Lógica)
3. Negación - not

Se Escriben Tal Como Están (En Minúsculas)

* OPERADOR AND:
Se le Conoce como una Multiplicación Lógica
Para Trabajar con el Operador AND se tienen que poner 2 Operandos
y estos Operandos tienen que ser 2 Valores Lógicos
y para que te retorne un Resultado Verdadero
tiene que comparar 2 Valores Verdaderos,
cualquier otra comparación de Operandos Diferentes
Retorna como Resultado Falso, como se Muestra a Continuación:

Operando1       Operador       Operando2       Resultado       Explicación
  True            and            True            True          1 x 1 = 1
  True            and            False           False         1 x 0 = 0
  False           and            True            False         0 x 1 = 0
  False           and            False           False         0 x 0 = 0

En la Programación:
TRUE tiene un Valor de 1
por lo que al multiplicar 1x1 es la única forma de que te de 1.

FALSE tiene un Valor de 0
por lo tanto todo lo que multipliques por cero te dará cero.

* OPERADOR OR
Se le Conoce como una Suma Lógica

Operando1       Operador       Operando2       Resultado       Explicación
  True             or            True            True           1 + 1 = 2
  True             or            False           True           1 + 0 = 1
  False            or            True            True           0 + 1 = 1
  False            or            False           False          0 + 0 = 0

* OPERADOR NOT

Si tenemos una Expresión que nos da como Resultado TRUE
pero lo negamos usando un NOT obtendremos un FALSE

Si tenemos una Expresión que nos da como Resultado FALSE
pero lo negamos usando un NOT obtendremos un TRUE

   Operando         Resultado
  not (True)          False
  not (False)         True

 ***  PRIORIDAD DE LOS OPERADORES LÓGICOS ***

 El Orden en que se Evalúan es el Siguiente:

 1. NOT
 2. AND
 3. OR

  ***  PRIORIDAD DE LOS OPERADORES EN GENERAL ***

 El Orden en que se Evalúan es el Siguiente:

 1. ()  Paréntesis de Adentro Hacia Afuera
 2. **  Exponenciación
 3. * , / , mod , not  Multiplicación, División, Modulo, Negación
 4. + , - , and   Suma, Resta, AND
 5. > , < , == , >= , <= , != , OR  Operadores Relacionales y el OR

"""

# Creamos Nuestras Variables

a = 10
b = 15
c = 20

# Comparamos si 10 es Menor que 15 y 15 es Menor que 20
resultado = ((a < b) and (b < c))

# Como 10 Si es Menor que 15 (True) y 15 Si es Menor que 20 (True) entonces nos retornara un True
print(resultado)

resultado = ((b > a) and (c > b))

print(resultado)

resultado = ((c > b) and (b > c))

print(resultado)
