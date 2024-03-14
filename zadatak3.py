lista = []
while(1):
    broj = input("Unesite brojeve: ")
    if(broj == 'Done'): 
        break
    try:
        num = float(broj)
        lista.append(num)
    except ValueError:
        print("Neispravan unos. Unesite broj: ")

print("Lista: ", lista)
print("Broj unesenih brojeva: ", len(lista))
print("Srednja vrijednost: ", sum(lista)/len(lista))
print("Minimalna vrijednost: ", min(lista))
print("Maksimalna vrijednost: ", max(lista))
lista.sort()
print("Sortirana lista: ", lista)