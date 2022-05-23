while True:
    input("Apasa orice tasta pentru a continua...")
    print()
    joc=input("Alege un joc(a=6/49 | b=5/40):")
    print()
    input("Apasa orice tasta pentru a cumpara biletele...")
    print()
    if joc == 'a':
        import random
        numere_random = []
        for i in range(0,49):
            nr = random.randint(1,99)
            numere_random.append(nr)
        v=[0]*6
        print("Alege numerele din bilet:")
        for i in range(6):
            v[i]=input("Nr."+str(i+1)+":")
    if joc == 'b':
        import random
        numere_random = []
        for i in range(0,40):
            nr = random.randint(1,99)
            numere_random.append(nr)
        v=[0]*5
        print("Alege numerele:")
        for i in range(5):
            v[i]=input("Nr."+str(i+1)+":")
    input("Apasa orice tasta pentru a continua...")
    print()
    extragere=input("Extragi numerele(da / nu):")
    print()
    if extragere == 'da':
        for i in range(len(numere_random)):
            print("El"+str(i+1)+":",numere_random[i])
    if extragere == 'nu':
        print("Multumim pentru atentia acordata pana acum!")
        exit(1)
    input("Apasa orice tasta pentru a vedea rezultatul...")
    print()
    k=0
    for i in range(len(numere_random)):
        for j in range(len(v)):
            if v[j]==numere_random[i]:
                k+=1
    if k==len(v):
        print("Bilet castigator!")
    if k!=len(v):
        print("Bilet NEcastigator!")
    print()
    input("Apasa orice tasta pentru a inchide programul!")
    print()
    exit(1)