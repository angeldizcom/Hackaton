"""
salas de juegos
preguntar la edad
< 4años = gratis
> 4 y < 18 son 5€
> 18 son 10€
"""
print('Kata3')

edad = input("Introduce tu edad: ")
edad = int(edad)

if(edad < 4 ):
    print("La entrada es gratuita.")
elif(edad >= 4 and edad <= 18):
    print("El precio de la entrada son 5€")
else:
    print("El precio de la entrada son 10€")