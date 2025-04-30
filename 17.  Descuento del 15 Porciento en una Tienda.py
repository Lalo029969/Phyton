''' Ejercicio #5
Una Tienda Ofrece un Descuento del 15% sobre el Total
de la Compra y un Cliente desea saber cuánto deberá pagar
finalmente por su compra (Despues del Descuento).
'''

print() # Salto de Linea

precio_inicial = float(input("Digite el Precio del Producto que Va a Comprar: $ "))

# Calculamos el Descuento del 15% :
descuento = precio_inicial * 15/100

# O Tambien lo Podemos Calcular Asi:
# descuento = precio * 0.15

# Aplicamos el Descuento al Precio Inicial
precio_final = precio_inicial - descuento

# Imprimimos el Precio Final con el Descuento Aplicado:
print (f"El Precio Final con Descuento es de: $ {precio_final:.2f}")

'''
Agregamos (:.2f) para que nos muestre unicamente 2 Decimales
En El Precio Final
'''



