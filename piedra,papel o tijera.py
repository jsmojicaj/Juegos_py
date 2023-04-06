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
print(f"El pc escogio {PC}:{PC_choise} \n")

if nombre=="papel":
    print("papel gana piedra")
elif nombre=="piedra":
    print("Piedra gana tijera")
elif nombre=="tijera":
    print("tijera gana papel")
else:
    print("ERROR! por favor,escoge: piedra, papel o tijera ")