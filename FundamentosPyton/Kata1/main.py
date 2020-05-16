print('Kata1')
"""
panaderia
pan = 3.49€
si no son frescas - 60%
"""

precio = 3.49
descuento = 0.4
precio_descuento = precio * descuento
numero_de_barras =input("Introduce el numero de barras vendidas: ")
total = int(numero_de_barras) * precio_descuento


print("Precio habitual " + str(precio))
print("Precio con descuento: " + str(precio_descuento))
print("Coste final: " + str(total))