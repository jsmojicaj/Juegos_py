import random
nombre=input("Escoge: piedra, papel o tijera: ")
print(f"has escogido {nombre}")

PC=random.randint(1,3)
if PC==1:
    PC_choise="piedra"
elif PC==2:
    PC_choise="papel"
elif PC==3:
    PC_choise="tijera"
if (nombre!="piedra") or (nombre!="papel") or (nombre!="tijera"):
    print("ERROR!")

print(f"Escogiste {nombre}")
print(f"El pc escogio {PC_choise} \n")

if nombre==PC_choise:
    print("Es empate!")
elif (nombre=="piedra" and PC_choise=="tijera") or (nombre=="tijera" and PC_choise=="papel") or (nombre=="papel" and PC_choise=="piedra"):
    print("Has ganado!")
else:
    print("Has perdido!")