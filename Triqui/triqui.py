
import random
TEMPLATE_FIELD=[[" "," "," "],[" "," "," "],[" "," "," "]]
TEMPLATE_FIELD_NUMBER = '|0|1|2|\n|3|4|5|\n|6|7|8|\n'
registro=[]
for i in range(4):
    casilla=int(input("Eres la x, Escoge un numero => "))
    TEMPLATE_FIELD_NUMBER=TEMPLATE_FIELD_NUMBER.replace(str(casilla),"-")

    if casilla<=2: TEMPLATE_FIELD[0][casilla]="x"
    elif casilla<=5: TEMPLATE_FIELD[1][casilla-3]="x"
    elif casilla<=8: TEMPLATE_FIELD[2][casilla-6]="x"
    else: "El numero no esta fuera del rango de las casillas"

    casilla_pc=int(random.uniform(0,8))
    while (casilla==casilla_pc) or (casilla_pc in registro): 
        casilla_pc=int(random.uniform(0,8))
        print(casilla_pc)
    TEMPLATE_FIELD_NUMBER=TEMPLATE_FIELD_NUMBER.replace(str(casilla_pc),"-")
    if casilla_pc<=2: TEMPLATE_FIELD[0][casilla_pc]="o"
    elif casilla_pc<=5: TEMPLATE_FIELD[1][casilla_pc-3]="o"
    elif casilla_pc<=8: TEMPLATE_FIELD[2][casilla_pc-6]="o"

    FIELD = f"|{TEMPLATE_FIELD[0][0]}|{TEMPLATE_FIELD[0][1]}|{TEMPLATE_FIELD[0][2]}|\n"\
            f"|{TEMPLATE_FIELD[1][0]}|{TEMPLATE_FIELD[1][1]}|{TEMPLATE_FIELD[1][2]}|\n"\
            f"|{TEMPLATE_FIELD[2][0]}|{TEMPLATE_FIELD[2][1]}|{TEMPLATE_FIELD[2][2]}|\n"

    registro.append(casilla)
    registro.append(casilla_pc)
    print(TEMPLATE_FIELD_NUMBER)
    print(FIELD)
    print(casilla_pc)


