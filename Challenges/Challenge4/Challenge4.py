#Exercise here ("https://drive.google.com/file/d/1OIOjRh-M858Hr3ALckAf54ptM3mpWptP/view?usp=sharing")

def tiene_cartas_altas(cartas_siguientes):
    for k in cartas_siguientes:
      if k in "A":
        return True
      elif k in "J":
        return True
      elif k in "Q":
        return True
      elif k in "K":
        return True
    return False


def juego(baraja):
    N_CARTAS = len(baraja)
    jugador_actual = 'jugador1'
    puntaje_jugador_1 = 0
    puntaje_jugador_2 = 0
    for i,j in enumerate(baraja):
        puntos = 0
        n_cartas_restantes = N_CARTAS - i - 1
        if j == 'A' and n_cartas_restantes >= 1 and not (tiene_cartas_altas(baraja[i+1])):
            puntos = 1
        if j == 'J' and n_cartas_restantes >= 2 and not (tiene_cartas_altas(baraja[i+1:i+3])):
            puntos = 2
        elif j == 'Q' and n_cartas_restantes >= 3 and not (tiene_cartas_altas(baraja[i+1:i+4])):
            puntos = 3
        elif j == 'K' and n_cartas_restantes >= 4 and not (tiene_cartas_altas(baraja[i+1:i+5])):
            puntos = 4

        if jugador_actual == 'jugador1':
            puntaje_jugador_1 += puntos
            jugador_actual = 'jugador2'

        else:
            puntaje_jugador_2 += puntos
            jugador_actual = 'jugador1'
            
    return puntaje_jugador_1, puntaje_jugador_2