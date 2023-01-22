n=int(input("Podaj liczbę: "))
dzielnik=1
licznik=1
while dzielnik < n:
    if n%dzielnik==0:
        licznik+=1
        dzielnik+=1
    else:
        dzielnik+=1
print("Liczba ", n,"ma ", licznik,"dzielniki/ów")
