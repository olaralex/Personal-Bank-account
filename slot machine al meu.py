import random
#CONSTANTE
balanta=int(input("Pune banii:"))
fructe=["sapte","banane","harbuz","clopot","bar","lamaie","portocala","pruna","cirese"]

el_11 = None
el_12 = None
el_13 = None
el_21 = None
el_22 = None
el_23 = None
el_31 = None
el_32 = None
el_33 = None

def joc():
    
    global balanta, el_11, el_12, el_13, el_21, el_22, el_23, el_31, el_32, el_33
    intrebare_joc=intreaba()
    while balanta!=0 and intrebare_joc==True:
        el_11 = invarte()
        el_12 = invarte()
        el_13 = invarte()
        el_21 = invarte()
        el_22 = invarte()
        el_23 = invarte()
        el_31 = invarte()
        el_32 = invarte()
        el_33 = invarte()
        afiseaza_rezultat()
        intrebare_joc=intreaba()
        
def intreaba():
    
    global balanta
    while True:
        raspuns = input("Ai $" + str(balanta) + ". Vrei sa joci? ")
        print()
        raspuns = raspuns.lower()
        if(raspuns == "da" or raspuns == "d"):
            return True
        elif(raspuns == "nu" or raspuns == "n"):
            print("Ai iesit din joc cu $" + str(balanta) + " in mana.")
            print()
            return False
        else:
            print("Raspuns Gresit")
            print()

def invarte():
    
    numarRandom = random.randint(0, 8)
    return fructe[numarRandom]

def afiseaza_rezultat():
    
    global balanta, el_11, el_12, el_13, el_21, el_22, el_23, el_31, el_32, el_33
    
    #SAPTE
    
    if((el_11 == "sapte") and (el_12 == "sapte")):
        win = 100
    elif((el_21 == "sapte") and (el_22 == "sapte")):
        win = 100
    elif((el_31 == "sapte") and (el_32 == "sapte")):
        win = 100
    elif((el_11 == "sapte") and (el_12 == "sapte")) and (el_13 == "sapte"):
        win = 200
    elif((el_21 == "sapte") and (el_22 == "sapte")) and (el_23 == "sapte"):
        win = 200
    elif((el_31 == "sapte") and (el_32 == "sapte")) and (el_33 == "sapte"):
        win = 200
    elif((el_11 == "sapte") and (el_22 == "sapte")):
        win = 100
    elif((el_31 == "sapte") and (el_22 == "sapte")):
        win = 100
    elif((el_11 == "sapte") and (el_22 == "sapte")) and (el_33 == "sapte"):
        win = 200
    elif((el_31 == "sapte") and (el_22 == "sapte")) and (el_13 == "sapte"):
        win = 200
    elif((el_21 == "sapte") and (el_12 == "sapte")):
        win = 100
    elif((el_21 == "sapte") and (el_32 == "sapte")):
        win = 100
    elif((el_11 == "sapte") and (el_12 == "sapte")) and (el_13 == "sapte") and (el_21 == "sapte") and (el_22 == "sapte") and (el_23 == "sapte") and (el_31 == "sapte") and (el_32 == "sapte") and (el_33 == "sapte"):
        win = 1000
    else:
        win = -5
    
    #BANANE
    
    if((el_11 == "banane") and (el_12 == "banane")):
        win = 20
    elif((el_21 == "banane") and (el_22 == "banane")):
        win = 20
    elif((el_31 == "banane") and (el_32 == "banane")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "banane")) and (el_13 == "banane"):
        win = 40
    elif((el_21 == "banane") and (el_22 == "banane")) and (el_23 == "banane"):
        win = 40
    elif((el_31 == "banane") and (el_32 == "banane")) and (el_33 == "banane"):
        win = 40
    elif((el_11 == "banane") and (el_22 == "banane")):
        win = 20
    elif((el_31 == "banane") and (el_22 == "banane")):
        win = 20
    elif((el_11 == "banane") and (el_22 == "banane")) and (el_33 == "banane"):
        win = 40
    elif((el_31 == "banane") and (el_22 == "banane")) and (el_13 == "banane"):
        win = 40
    elif((el_21 == "banane") and (el_12 == "banane")):
        win = 20
    elif((el_21 == "banane") and (el_32 == "banane")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "banane")) and (el_13 == "banane") and (el_21 == "banane") and (el_22 == "banane") and (el_23 == "banane") and (el_31 == "banane") and (el_32 == "banane") and (el_33 == "banane"):
        win = 80
    else:
        win = -5
    
    #HARBUZ
    
    if((el_11 == "harbuz") and (el_12 == "harbuz")):
        win = 20
    elif((el_21 == "harbuz") and (el_22 == "harbuz")):
        win = 20
    elif((el_31 == "harbuz") and (el_32 == "harbuz")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "harbuz")) and (el_13 == "harbuz"):
        win = 40
    elif((el_21 == "harbuz") and (el_22 == "harbuz")) and (el_23 == "harbuz"):
        win = 40
    elif((el_31 == "harbuz") and (el_32 == "harbuz")) and (el_33 == "harbuz"):
        win = 40
    elif((el_11 == "harbuz") and (el_22 == "harbuz")):
        win = 20
    elif((el_31 == "harbuz") and (el_22 == "harbuz")):
        win = 20
    elif((el_11 == "harbuz") and (el_22 == "harbuz")) and (el_33 == "harbuz"):
        win = 40
    elif((el_31 == "harbuz") and (el_22 == "harbuz")) and (el_13 == "harbuz"):
        win = 40
    elif((el_21 == "harbuz") and (el_12 == "harbuz")):
        win = 20
    elif((el_21 == "harbuz") and (el_32 == "harbuz")):
        win = 20
    elif((el_11 == "harbuz") and (el_12 == "harbuz")) and (el_13 == "harbuz") and (el_21 == "harbuz") and (el_22 == "harbuz") and (el_23 == "harbuz") and (el_31 == "harbuz") and (el_32 == "harbuz") and (el_33 == "harbuz"):
        win = 80
    else:
        win = -5
        
    #CLOPOT
    
    if((el_11 == "clopot") and (el_12 == "clopot")):
        win = 40
    elif((el_21 == "clopot") and (el_22 == "clopot")):
        win = 40
    elif((el_31 == "clopot") and (el_32 == "clopot")):
        win = 40
    elif((el_11 == "clopot") and (el_12 == "clopot")) and (el_13 == "clopot"):
        win = 80
    elif((el_21 == "clopot") and (el_22 == "clopot")) and (el_23 == "clopot"):
        win = 80
    elif((el_31 == "clopot") and (el_32 == "clopot")) and (el_33 == "clopot"):
        win = 80
    elif((el_11 == "clopot") and (el_22 == "clopot")):
        win = 40
    elif((el_31 == "clopot") and (el_22 == "clopot")):
        win = 40
    elif((el_11 == "clopot") and (el_22 == "clopot")) and (el_33 == "clopot"):
        win = 80
    elif((el_31 == "clopot") and (el_22 == "clopot")) and (el_13 == "clopot"):
        win = 80
    elif((el_21 == "clopot") and (el_12 == "clopot")):
        win = 80
    elif((el_21 == "clopot") and (el_32 == "clopot")):
        win = 40
    elif((el_11 == "clopot") and (el_12 == "clopot")) and (el_13 == "clopot") and (el_21 == "clopot") and (el_22 == "clopot") and (el_23 == "clopot") and (el_31 == "clopot") and (el_32 == "clopot") and (el_33 == "clopot"):
        win = 120
    else:
        win = -5
    
    #BAR
    
    if((el_11 == "bar") and (el_12 == "bar")):
        win = 20
    elif((el_21 == "bar") and (el_22 == "bar")):
        win = 20
    elif((el_31 == "bar") and (el_32 == "bar")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "bar")) and (el_13 == "bar"):
        win = 40
    elif((el_21 == "bar") and (el_22 == "bar")) and (el_23 == "bar"):
        win = 40
    elif((el_31 == "bar") and (el_32 == "bar")) and (el_33 == "bar"):
        win = 40
    elif((el_11 == "bar") and (el_22 == "bar")):
        win = 20
    elif((el_31 == "bar") and (el_22 == "bar")):
        win = 20
    elif((el_11 == "bar") and (el_22 == "bar")) and (el_33 == "bar"):
        win = 40
    elif((el_31 == "bar") and (el_22 == "bar")) and (el_13 == "bar"):
        win = 40
    elif((el_21 == "bar") and (el_12 == "bar")):
        win = 20
    elif((el_21 == "bar") and (el_32 == "bar")):
        win = 20
    elif((el_11 == "bar") and (el_12 == "bar")) and (el_13 == "bar") and (el_21 == "bar") and (el_22 == "bar") and (el_23 == "bar") and (el_31 == "harbuz") and (el_32 == "bar") and (el_33 == "bar"):
        win = 80
    else:
        win = -5
    
    #LAMAIE
    
    if((el_11 == "lamaie") and (el_12 == "lamaie")):
        win = 40
    elif((el_21 == "lamaie") and (el_22 == "lamaie")):
        win = 40
    elif((el_31 == "lamaie") and (el_32 == "lamaie")):
        win = 40
    elif((el_11 == "banane") and (el_12 == "lamaie")) and (el_13 == "lamaie"):
        win = 80
    elif((el_21 == "lamaie") and (el_22 == "lamaie")) and (el_23 == "lamaie"):
        win = 80
    elif((el_31 == "lamaie") and (el_32 == "lamaie")) and (el_33 == "lamaie"):
        win = 80
    elif((el_11 == "lamaie") and (el_22 == "lamaie")):
        win = 40
    elif((el_31 == "lamaie") and (el_22 == "lamaie")):
        win = 40
    elif((el_11 == "lamaie") and (el_22 == "lamaie")) and (el_33 == "lamaie"):
        win = 80
    elif((el_31 == "lamaie") and (el_22 == "lamaie")) and (el_13 == "lamaie"):
        win = 80
    elif((el_21 == "lamaie") and (el_12 == "lamaie")):
        win = 40
    elif((el_21 == "lamaie") and (el_32 == "lamaie")):
        win = 40
    elif((el_11 == "lamaie") and (el_12 == "lamaie")) and (el_13 == "lamaie") and (el_21 == "lamaie") and (el_22 == "lamaie") and (el_23 == "lamaie") and (el_31 == "harbuz") and (el_32 == "lamaie") and (el_33 == "lamaie"):
        win = 120
    else:
        win = -5
    
    #PORTOCALA

    if((el_11 == "portocala") and (el_12 == "portocala")):
        win = 20
    elif((el_21 == "portocala") and (el_22 == "portocala")):
        win = 20
    elif((el_31 == "portocala") and (el_32 == "portocala")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "portocala")) and (el_13 == "portocala"):
        win = 40
    elif((el_21 == "portocala") and (el_22 == "portocala")) and (el_23 == "portocala"):
        win = 40
    elif((el_31 == "portocala") and (el_32 == "portocala")) and (el_33 == "portocala"):
        win = 40
    elif((el_11 == "portocala") and (el_22 == "portocala")):
        win = 20
    elif((el_31 == "portocala") and (el_22 == "portocala")):
        win = 20
    elif((el_11 == "portocala") and (el_22 == "portocala")) and (el_33 == "portocala"):
        win = 40
    elif((el_31 == "portocala") and (el_22 == "portocala")) and (el_13 == "portocala"):
        win = 40
    elif((el_21 == "portocala") and (el_12 == "portocala")):
        win = 20
    elif((el_21 == "portocala") and (el_32 == "portocala")):
        win = 20
    elif((el_11 == "portocala") and (el_12 == "portocala")) and (el_13 == "portocala") and (el_21 == "portocala") and (el_22 == "portocala") and (el_23 == "portocala") and (el_31 == "harbuz") and (el_32 == "portocala") and (el_33 == "portocala"):
        win = 80
    else:
        win = -5

    #PRUNA

    if((el_11 == "pruna") and (el_12 == "pruna")):
        win = 40
    elif((el_21 == "pruna") and (el_22 == "pruna")):
        win = 40
    elif((el_31 == "pruna") and (el_32 == "pruna")):
        win = 40
    elif((el_11 == "banane") and (el_12 == "pruna")) and (el_13 == "pruna"):
        win = 80
    elif((el_21 == "pruna") and (el_22 == "pruna")) and (el_23 == "pruna"):
        win = 80
    elif((el_31 == "pruna") and (el_32 == "pruna")) and (el_33 == "pruna"):
        win = 80
    elif((el_11 == "pruna") and (el_22 == "pruna")):
        win = 40
    elif((el_31 == "pruna") and (el_22 == "pruna")):
        win = 40
    elif((el_11 == "pruna") and (el_22 == "pruna")) and (el_33 == "pruna"):
        win = 80
    elif((el_31 == "pruna") and (el_22 == "pruna")) and (el_13 == "pruna"):
        win = 80
    elif((el_21 == "pruna") and (el_12 == "pruna")):
        win = 40
    elif((el_21 == "pruna") and (el_32 == "pruna")):
        win = 40
    elif((el_11 == "pruna") and (el_12 == "pruna")) and (el_13 == "pruna") and (el_21 == "pruna") and (el_22 == "pruna") and (el_23 == "pruna") and (el_31 == "harbuz") and (el_32 == "pruna") and (el_33 == "pruna"):
        win = 120
    else:
        win = -5
    
    #PRUNA

    if((el_11 == "pruna") and (el_12 == "pruna")):
        win = 20
    elif((el_21 == "pruna") and (el_22 == "pruna")):
        win = 20
    elif((el_31 == "pruna") and (el_32 == "pruna")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "pruna")) and (el_13 == "pruna"):
        win = 40
    elif((el_21 == "pruna") and (el_22 == "pruna")) and (el_23 == "pruna"):
        win = 40
    elif((el_31 == "pruna") and (el_32 == "pruna")) and (el_33 == "pruna"):
        win = 40
    elif((el_11 == "pruna") and (el_22 == "pruna")):
        win = 20
    elif((el_31 == "pruna") and (el_22 == "pruna")):
        win = 20
    elif((el_11 == "pruna") and (el_22 == "pruna")) and (el_33 == "pruna"):
        win = 40
    elif((el_31 == "pruna") and (el_22 == "pruna")) and (el_13 == "pruna"):
        win = 40
    elif((el_21 == "pruna") and (el_12 == "pruna")):
        win = 20
    elif((el_21 == "pruna") and (el_32 == "pruna")):
        win = 20
    elif((el_11 == "pruna") and (el_12 == "pruna")) and (el_13 == "pruna") and (el_21 == "pruna") and (el_22 == "pruna") and (el_23 == "pruna") and (el_31 == "harbuz") and (el_32 == "pruna") and (el_33 == "pruna"):
        win = 80
    else:
        win = -5
    
    #CIRESE

    if((el_11 == "cirese") and (el_12 == "cirese")):
        win = 20
    elif((el_21 == "cirese") and (el_22 == "cirese")):
        win = 20
    elif((el_31 == "cirese") and (el_32 == "cirese")):
        win = 20
    elif((el_11 == "banane") and (el_12 == "cirese")) and (el_13 == "cirese"):
        win = 40
    elif((el_21 == "cirese") and (el_22 == "cirese")) and (el_23 == "cirese"):
        win = 40
    elif((el_31 == "cirese") and (el_32 == "cirese")) and (el_33 == "cirese"):
        win = 40
    elif((el_11 == "cirese") and (el_22 == "cirese")):
        win = 20
    elif((el_31 == "cirese") and (el_22 == "cirese")):
        win = 20
    elif((el_11 == "cirese") and (el_22 == "cirese")) and (el_33 == "cirese"):
        win = 40
    elif((el_31 == "cirese") and (el_22 == "cirese")) and (el_13 == "cirese"):
        win = 40
    elif((el_21 == "cirese") and (el_12 == "cirese")):
        win = 20
    elif((el_21 == "cirese") and (el_32 == "cirese")):
        win = 20
    elif((el_11 == "cirese") and (el_12 == "cirese")) and (el_13 == "cirese") and (el_21 == "cirese") and (el_22 == "cirese") and (el_23 == "cirese") and (el_31 == "harbuz") and (el_32 == "cirese") and (el_33 == "cirese"):
        win = 80
    else:
        win = -5

    #AFISAJ
    
    balanta += win
    if(win > 0):
        print(el_11 + '\t' + el_12 + '\t' + el_13)
        print(el_21 + '\t' + el_22 + '\t' + el_23)
        print(el_31 + '\t' + el_32 + '\t' + el_33)
        print(' -- Ai castigat $' + str(win))
    else:
        print(el_11 + '\t' + el_12 + '\t' + el_13)
        print(el_21 + '\t' + el_22 + '\t' + el_23)
        print(el_31 + '\t' + el_32 + '\t' + el_33)
        print(' -- Ai pierdut')
        
joc()