import random

def esquivar(probabilidad):
    return random.choice(probabilidad)

def combate(HP1, HP2, esquivo1, esquivo2):
    while HP1 > 0 and HP2 > 0:
        if not esquivar(esquivo2):
            HP2 -= 10 
            print("Jugador 1 ataca a Jugador 2. HP2 ahora es:", HP2)
        else:
            print("Jugador 2 esquivó el ataque de Jugador 1.")

        if HP2 <= 0:
            print("¡Jugador 1 es el ganador!")
            break

        if not esquivar(esquivo1):
            HP1 -= 10  
            print("Jugador 2 ataca a Jugador 1. HP1 ahora es:", HP1)
        else:
            print("Jugador 1 esquivó el ataque de Jugador 2.")

        if HP1 <= 0:
            print("¡Jugador 2 es el ganador!")
            break

HP1 = int(input("HP1: "))
HP2 = int(input("HP2: "))

esquivo1 = [True, False]
esquivo2 = [True, False]

combate(HP1, HP2, esquivo1, esquivo2)



dias_3 = [i, dia for i in lista_dias_semana if i % 2 == 0]
print(dias_3)