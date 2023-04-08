import random
nombre=input("Escoge: piedra, papel o tijera => ")
nombre=nombre.lower() #Hace que las mayusculas se vuelvan minusculas. 
opciones=("piedra","papel","tijera") #tupla de las opciones
PC_choise=random.choice(opciones)

while nombre not in opciones:
    print("ERROR!")
    nombre=input("por favor,escoge: piedra, papel o tijera => ")

print(f"\nEscogiste {nombre}")
print(f"El pc escogio {PC_choise} \n")

if nombre==PC_choise:
    print("Es empate!")
elif (nombre=="piedra" and PC_choise=="tijera") or (nombre=="tijera" and PC_choise=="papel") or (nombre=="papel" and PC_choise=="piedra"):
    print("Has ganado!")
else:
    print("Has perdido!")