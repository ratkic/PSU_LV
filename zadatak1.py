# radniSati = float(input("Unesi radne sate: "))
# iznos = float(input("Unesi eure/h: "))
# zarada = radniSati * iznos
# print(zarada, " eura/h")

def total_euro(sati, iznos):
    return sati * iznos

def main():
     sati = float(input("Unesi radne sate: "))
     iznos = float(input("Unesi eure/h: "))
     zarada = total_euro(sati, iznos)
     print(zarada)

main()