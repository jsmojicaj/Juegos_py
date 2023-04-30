
import random
def evaluate(state):
    triples = [state[0:3], state[3:6], state[6:9], state[::3], state[1::3], state[2::3], [state[0], state[4], state[8]], [state[2], state[4], state[6]]]
    if ["x","x","x"] in triples:
        return 100
    elif ["o","o","o"] in triples:
        return -100
    else:
        return 0
    
def minimax(state, depth, maximizing_player):
    if depth == 0 or ["x","x","x"] in triples or ["o","o","o"] in triples:
        return evaluate(state), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for i in range(9):
            if state[i] == " ":
                state[i] = "x"
                eval, _ = minimax(state, depth-1, False)
                state[i] = " "
                if eval > max_eval:
                    max_eval = eval
                    best_move = i
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for i in range(9):
            if state[i] == " ":
                state[i] = "o"
                eval, _ = minimax(state, depth-1, True)
                state[i] = " "
                if eval < min_eval:
                    min_eval = eval
                    best_move = i
        return min_eval, best_move
TEMPLATE_FIELD=[" "," "," "," "," "," "," "," "," "]
TEMPLATE_FIELD_NUMBER = '|0|1|2|\n|3|4|5|\n|6|7|8|\n'
registro=[]
resultado="vacio"
while resultado=="vacio":
    casilla=int(input("Eres la x, Escoge un numero => "))
    while casilla in registro: casilla=int(input("Ya escogieron esa casilla,escoge un número disponible => "))
    while (casilla<0) or (casilla>8): casilla=int(input("El numero esta fuera del rango de las casillas, escoga un número dentro del rango 0-8 y que no se haya escogido => "))
    TEMPLATE_FIELD_NUMBER=TEMPLATE_FIELD_NUMBER.replace(str(casilla),"-")

    if casilla<=2: TEMPLATE_FIELD[casilla]="x"
    elif casilla<=5: TEMPLATE_FIELD[casilla]="x"
    elif casilla<=8: TEMPLATE_FIELD[casilla]="x"

    triples = [TEMPLATE_FIELD[0:3], TEMPLATE_FIELD[3:6], TEMPLATE_FIELD[6:9], TEMPLATE_FIELD[::3], TEMPLATE_FIELD[1::3],
            TEMPLATE_FIELD[2::3], [TEMPLATE_FIELD[0],TEMPLATE_FIELD[4],TEMPLATE_FIELD[8]],
            [TEMPLATE_FIELD[2],TEMPLATE_FIELD[4],TEMPLATE_FIELD[6]]]
    if ["x","x","x"] in triples: resultado="Tu ganas!"

    casilla_pc=int(random.uniform(0,8))
    while (casilla==casilla_pc) or (casilla_pc in registro): 
        casilla_pc=int(random.uniform(0,8))
        if len(registro)>=7: break

    TEMPLATE_FIELD_NUMBER=TEMPLATE_FIELD_NUMBER.replace(str(casilla_pc),"-")
    if casilla_pc<=2: TEMPLATE_FIELD[casilla_pc]="o"
    elif casilla_pc<=5: TEMPLATE_FIELD[casilla_pc]="o"
    elif casilla_pc<=8: TEMPLATE_FIELD[casilla_pc]="o"

    FIELD = f"|{TEMPLATE_FIELD[0]}|{TEMPLATE_FIELD[1]}|{TEMPLATE_FIELD[2]}|\n"\
            f"|{TEMPLATE_FIELD[3]}|{TEMPLATE_FIELD[4]}|{TEMPLATE_FIELD[5]}|\n"\
            f"|{TEMPLATE_FIELD[6]}|{TEMPLATE_FIELD[7]}|{TEMPLATE_FIELD[8]}|\n"

    registro.append(casilla)
    registro.append(casilla_pc)
    print(TEMPLATE_FIELD_NUMBER)
    print(FIELD)
    
    if ["o","o","o"] in triples: resultado="Gana el PC"
    if len(registro)>8: resultado="Empate"
    if resultado != "vacio": print(resultado)



