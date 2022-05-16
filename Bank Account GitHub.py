pin = input("PIN:")

sold = 0

meniu = {}
meniu[1] = "Show Sold"
meniu[2] = "Deposit"
meniu[3] = "Withdraw"
meniu[4] = "Delete Account"
meniu[5] = "Exit"

def afisare_sold():
    global sold
    print("Sold-ul tau este:",sold)
    
def deposit():
    global sold
    global trys
    trys = 5
    global ver_pin
    ver_pin = input("Introduceti PIN-ul:")
    while pin != ver_pin:
        print("PIN Gresit!")
        print("Mai ai ",trys," trys!")
        ver_pin = input("Introduceti din nou PIN-ul:")
        trys = trys - 1

        if trys == 0:
            del_acc_urgenta()
    
    global deposit_sold
    deposit_sold = 0
    deposit_sold = int(input("Alege suma (in lei):"))
    sold = sold + deposit_sold


def withdraw():
    global sold
    trys = 5
    ver_pin = input("Introduceti PIN-ul:")
    while pin != ver_pin:
        print("PIN Gresit!")
        print("Mai ai ",trys," trys!")
        ver_pin = input("Introduceti din nou PIN-ul:")
        trys = trys - 1

        if trys == 0:
            del_acc_urgenta()
            
    global withdraw_sold
    withdraw_sold = 0
    withdraw_sold = int(input("Alege suma (in lei):"))
    if withdraw_sold > sold:
        print("Fonduri Insuficiente!")
    else:
        sold = sold - withdraw_sold

def del_acc():
    global sold
    global pin
    del sold
    del pin
    print("Contul tau a fost sters integral.")

def del_acc_urgenta():
    print("Ai depasit numarul de trys, contul tau de va autodistruge!")
    del_acc()
    exit(1)

def iesire():
    print("Ai iesit din aplicatie, o zi buna!")
    exit(1)

while True:
    for i in meniu:
        print(i,'. ',meniu[i], sep='')

    var = input("Alege un dintre varinate:")

    if var == '1':
        afisare_sold()
    if var == '2':
        deposit()
    if var == '3':
        withdraw()
    if var == '4':
        del_acc()
    if var == '5':
        iesire()