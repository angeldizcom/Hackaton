from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if((player.lower() == options[0].lower() and ai.lower() == options[0].lower()) or (player.lower() == options[1].lower() and ai.lower() == options[1].lower()) or (player.lower() == options[2].lower() and ai.lower() == options[2].lower())):
        resultado = "Empate!"
    elif ((player.lower() == options[0].lower() and ai.lower() == options[1].lower()) or (player.lower() == options[1].lower() and ai.lower() == options[2].lower()) or (player.lower() == options[2].lower() and ai.lower() == options[0].lower())):
        resultado = "Perdiste!"
    else: 
        resultado = "Ganaste!"
    return resultado

# Entry Point
def Game():
    #
    #
    global options
    is_valid = True
    while is_valid:
        player=input("Seleccione una de los siguetes opciones para jugar ():\n -Piedra\n-Papel\n-Tijeras\n")
        if(player.lower() == options[0].lower() or player.lower() == options[1].lower() or player.lower() == options[2].lower()):
            is_valid = False
        else:
            print("Opcion no valida")
    #
    #
    ai_option = randint(0,2)
    if(ai_option == 0):
        ai = options[0]
    elif(ai_option == 1):
        ai = options[1]
    else:
        ai = options[2]
    print("la opcion de la ai es: " +str(ai))
    winner = quienGana(player, ai)

    print(winner)

Game()