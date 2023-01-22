import math
f = float(input('Podaj liczbę zmiennoprzecinkową: '))
print(int((f-(f-math.floor(f))) % 10), 'i' ,int(round(f-math.floor(f),4) // 0.1))