n = int(input("Podaj n liczb do wczytania, a następnie wartości: "))
liczba = int(input("Podaj liczbę: "))
max = liczba
min = liczba
i = 1

while i < n:
    liczba = int(input("Podaj liczbę: "))
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba
    i += 1

print(max)
print(min)