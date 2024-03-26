#radniSati = float(input("Radni sati: "))
#iznos = float(input("eura/h: "))
#zarada = radniSati * iznos
#print(zarada)

def izracunajIznos(sati, placa):
    total = sati * placa
    return total

def main():
    sati = float(input("Radni sati: "))
    placa = float(input("eura/h: "))
    zarada = izracunajIznos(sati, placa)
    print(zarada, " eura")


main()