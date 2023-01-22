n=int(input("Podaj liczbę, która ma zostać spotęgowana: "))
m=int(input("Podaj liczbę, która będzie potęgą: "))
licznik=1
wynik=n
while licznik < m:
    wynik*=n
    licznik+=1
print("Wynik ", n,"do potęgi ", m,"wynosi: ", wynik)
