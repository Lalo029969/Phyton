# OPERADORES RELACIONALES

'''

* Se utilizan para Establecer una Relación entre 2 Valores.

* Compara Valores entre sí y esta comparación
 produce un Resultado de Certeza o Falsedad
 (Verdadero o Falso).

* Tienen el Mismo Nivel de Prioridad en su Evaluación.

* Los Operadores Relacionales Tienen Menor Prioridad que
 los Operadores Aritméticos.

>   Mayor Que
<   Menor Que
>=  Mayor o Igual Que
<=  Menor o Igual Que
!=  Diferente (Compara si 2 Valores son Diferentes uno de otro)
=   Igual (Asigna un Valor a la Variable)
==  Igualdad (Compara si 2 Valores son Iguales)

'''

# Creamos Nuestras Variables y le Asignamos un Valor

Variable1 = 6
Variable2 = 5

# MAYOR QUE

#Comparara Si el Valor Almacenado en la Variable1 es Mayor que la Variable2
resultado = (Variable1 > Variable2)

#Si la Variable1 es Menor que la Variable2 se Imprime False
print (resultado)

# MENOR QUE

resultado = (Variable1 < Variable2)
#Si la Variable1 es Mayor que la Variable2 se Imprime True
print (resultado)


# MAYOR O IGUAL QUE

#Comparara Si el Valor Almacenado en la Variable1 es Mayor o Igual que la Variable2
resultado = (Variable1 >= Variable2)

#Si la Variable1 es Mayor o Igual que la Variable2 se Imprime True, si no lo es se imprime False
print (resultado)

# MENOR O IGUAL QUE

#Comparara Si el Valor Almacenado en la Variable1 es Menor o Igual que la Variable2
resultado = (Variable1 <= Variable2)

#Si la Variable1 es Menor o Igual que la Variable2 se Imprime True, si no lo es se imprime False
print (resultado)

resultado = (Variable1 == Variable2)

