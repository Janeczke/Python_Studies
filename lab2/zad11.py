n=int(input("Podaj liczbę: "))
dzielnik=1
licznik_dzielnikow=0
while dzielnik < n:
    if n%dzielnik==0:
        licznik_dzielnikow+=1
        dzielnik+=1
    else:
        dzielnik+=1
wynik=licznik_dzielnikow
if wynik <= 2:
    print("Liczba ", n,"jest liczbą pierwszą")
else:
    print("Liczba ", n,"jest liczbą złożoną")
