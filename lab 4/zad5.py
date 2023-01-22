L_sreniej= 0
liczba_ocen = int(input('podaj liczbe ocen do sredniej: '))
for i in range(liczba_ocen):
    ocena = int(input(f'podaj ocene {i+1} do sredniej: '))
    L_sreniej +=ocena
avg = L_sreniej/liczba_ocen
print(f'średnia to {avg}')