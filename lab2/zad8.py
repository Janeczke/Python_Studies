n=int(input("Podaj liczbę: "))
wynik=0
i=1
silnia=1
while i < n:
    i+=1
    silnia=silnia*i
wynik=silnia
print("Wynik działania ", n,"! wynosi: ", wynik)
