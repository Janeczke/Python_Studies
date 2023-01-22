R = int(input('Podaj rok: '))
if R % 4==0 and R % 100 != 0:
    print("jest przestępny")
elif R % 100==0:
    print("nie jest przestępny")
elif R % 400==0:
    print("jest przestępny")
else:
    print("nie jest przestępny")