import random
nombre=input("Escoge: piedra, papel o tijera => ")
nombre=nombre.lower() #Hace que las mayusculas se vuelvan minusculas. 
opciones=("piedra","papel","tijera") #tupla de las opciones
PC=random.randint(1,3)
if PC==1:
    PC_choise=opciones[0]
elif PC==2:
    PC_choise=opciones[1]
elif PC==3:
    PC_choise=opciones[2]

if nombre in opciones:
    verificacion=True
else:
    verificacion=False
    while verificacion==False:
        print("ERROR!")
        nombre=input("por favor,escoge: piedra, papel o tijera => ")
        if nombre in opciones:
            verificacion=True
            break

print(f"\nEscogiste {nombre}")
print(f"El pc escogio {PC_choise} \n")

if nombre==PC_choise:
    print("Es empate!")
elif (nombre=="piedra" and PC_choise=="tijera") or (nombre=="tijera" and PC_choise=="papel") or (nombre=="papel" and PC_choise=="piedra"):
    print("Has ganado!")
else:
    print("Has perdido!")