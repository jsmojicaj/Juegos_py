
#TEMPLATE_FIELD = '| | | |\n| | | |\n| | | |\n'
TEMPLATE_FIELD=[[" "," "," "],[" "," "," "],[" "," "," "]]
TEMPLATE_FIELD_NUMBER = '|0|1|2|\n|3|4|5|\n|6|7|8|\n'
casilla=int(input("Escoge un numero => "))
TEMPLATE_FIELD_NUMBER=TEMPLATE_FIELD_NUMBER.replace(str(casilla),"-")

FIELD = f"|{TEMPLATE_FIELD[0][0]}|{TEMPLATE_FIELD[0][1]}|{TEMPLATE_FIELD[0][2]}|\n"\
        f"|{TEMPLATE_FIELD[1][0]}|{TEMPLATE_FIELD[1][1]}|{TEMPLATE_FIELD[1][2]}|\n"\
        f"|{TEMPLATE_FIELD[2][0]}|{TEMPLATE_FIELD[2][1]}|{TEMPLATE_FIELD[2][2]}|\n"
print(TEMPLATE_FIELD_NUMBER,FIELD)
