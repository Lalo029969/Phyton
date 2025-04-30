# CONDICIONALES COMBINADOS

""" Vamos a Validar si el Usuario es Mayor de Edad """

edad = int(input("Ingrese Su Edad: "))

if edad>=18 and edad<100:
    print ("El Valor Ingresado es una Edad Lógica")
    print ("Usted Es Mayor de Edad")

elif edad>=0 and edad<18:
    print("Usted NO Es Mayor de Edad")

else:
    print("¿Estás Imbecil?")
    print("Esa Edad No Existe")
