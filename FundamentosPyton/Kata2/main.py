"""
almacena cadena contraseña en variable y compararla
"""
print('Kata2')

password = "password"
input_password = input("Introduzca contraseña: ")
input_password = input_password.lower()

if(input_password == password):
    print("Acceso concedido")
else:
    print("Acceso denegado")