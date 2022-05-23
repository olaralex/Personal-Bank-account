import random
import time

elemente = ["Piatra", "Foarfeca", "Hartie"]

scor_user = 0
scor_pc = 0

input("Apasa ENTER pentru a incepe...")

while True:
    print("Alege una dintre varainte (numarul):")
    for i in range(len(elemente)):
        print(str(i+1)+". "+elemente[i])
    
    var = input("Alege o varianta:")

    alegere = elemente[int(var)-1]

    while alegere not in elemente:
        print("Alegere gresita!")
        var = input("Alege o varinata valida:")
        alegere = elemente[int(var)-1]

    alegere_pc = random.choice(elemente)

    for i in range(3):
        print(3-i,"...")
        time.sleep(2)

    print("TU","\t","PC")
    print(alegere,"\t",alegere_pc)

    #piatra

    if alegere == elemente[0] and alegere_pc == elemente[0]:
        print("Remiza")
    if alegere == elemente[0] and alegere_pc == elemente[1]:
        print("Ai castigat!")
        scor_user += 1
    if alegere == elemente[0] and alegere_pc == elemente[2]:
        print("Am castigat!")
        scor_pc += 1
    
    #foarfeca

    if alegere == elemente[1] and alegere_pc == elemente[1]:
        print("Remiza")
    if alegere == elemente[1] and alegere_pc == elemente[2]:
        print("Ai castigat!")
        scor_user += 1
    if alegere == elemente[1] and alegere_pc == elemente[0]:
        print("Am castigat!")
        scor_pc += 1

    #hartie

    if alegere == elemente[2] and alegere_pc == elemente[2]:
        print("Remiza")
    if alegere == elemente[2] and alegere_pc == elemente[0]:
        print("Ai castigat!")
        scor_user += 1
    if alegere == elemente[2] and alegere_pc == elemente[1]:
        print("Am castigat!")
        scor_pc += 1

    print("Scorul Este:")
    print(scor_user,"-",scor_pc)

    joc_nou = input("Mai vrei sa joci?(da/nu)")
    if joc_nou.upper() == 'DA':
        continue
    if joc_nou.upper() == 'NU':
        print("Ai iesit din joc!")
        print("Scorul a fost:")
        print(scor_user,"-",scor_pc)
        break