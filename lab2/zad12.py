for n in range(1,201):
    dzielnik=1
    licznik_dzielnikow=0
    while dzielnik < n:
        if n%dzielnik==0:
            licznik_dzielnikow+=1
            dzielnik+=1
        else:
            dzielnik+=1
    wynik=licznik_dzielnikow
    if wynik <= 1:
        print(n, end=" ")