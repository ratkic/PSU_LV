try:
    broj = float(input("Unesi broj: "))
    if broj < 0.0 or broj > 1.0:
        print("Broj je izvan intervala.")
    #elif broj > 0.0 or broj < 1.0 :  
    else:
        if broj >= 0.9:
            print('A')
        elif broj >= 0.8:
            print('B')
        elif broj >= 0.7:
            print('C')
        elif broj >= 0.6:
            print('D')
        elif broj < 0.6:
            print('F')
except:
    print("Nije unesen broj.")




#primjer sa funkcijom
def ispisOcjene(ocjene):
    if ocjene >= 0.9:
        return 'A'
    elif ocjene >= 0.8:
        return 'B'
    elif ocjene >= 0.7:
        return 'C'
    elif ocjene >= 0.6:
        return 'D'
    elif ocjene < 0.6:
        return 'F'
    
try:
    ocjene = float(input("Unesi ocjenu: "))
    if(ocjene < 0.0 or ocjene > 1.0):
        print("Izvan intervala.")
    else:
        ispis = ispisOcjene(ocjene)
        print(ispis)
except:
    print("Krivi unos.")

