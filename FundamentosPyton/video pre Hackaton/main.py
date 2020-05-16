'''
Esto es un adelanto en hackaton , comentario en bloque
'''
nombre = 'Angel Diaz'
edad = 15
esta_Trabajando = True # False
dato = input ('Introducir un dato: ')

print(dato)

print(edad)

if( edad >= 18 ):
    print('mayor')
else:
    print('menor')

def cuadrado(x):
    return x * x

cuadrado_de_dos = cuadrado(2)
print(cuadrado_de_dos)

for valor in (1,2,3,4):
    print(valor)
