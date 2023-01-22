import math
f = float(input('Podaj liczbę f zmiennoprzecinkową: '))
g = float(input('Podaj liczbę g zmiennoprzecinkową: '))

cf = f-(f-math.floor(f))
f = round(f-math.floor(f),3)
cg = g-(g-math.floor(g))
g = round(g-math.floor(g),3)

print(cg+f)
print(cf+g)