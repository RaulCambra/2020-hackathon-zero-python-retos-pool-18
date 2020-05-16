import random

options = ["piedra", "papel", "tijeras"]

resultados = ["Empate!","Ganaste!","Perdiste!"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player.lower() == options[0]:
        if ai.lower() == options[0]:
            return resultados[0]
        elif ai.lower() == options[1]:
            return resultados[2]
        elif ai.lower() == options[2]:
            return resultados[1]
        else:
            return 'Otra opcion'
    elif player.lower() == options[1]:
        if ai.lower() == options[0]:
            return resultados[1]
        elif ai.lower() == options[1]:
            return resultados[0]
        elif ai.lower() == options[2]:
            return resultados[2]
        else:
            return 'Otra opcion'
    elif player.lower() == options[2]:
        if ai.lower() == options[0]:
            return resultados[2]
        elif ai.lower() == options[1]:
            return resultados[1]
        elif ai.lower() == options[2]:
            return resultados[0]
        else:
            return 'Otra opcion'
    else:
        return 'Otra opcion'

# Entry Point
def Game():
    player = input("inserte Piedra, Papel o Tijeras ")
    ai = options[random.randint(0, 2)]
    print(ai)
    
    winner = quienGana(player, ai)

    print(winner)

Game()
