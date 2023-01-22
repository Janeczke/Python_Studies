from math import sin
n = int(input("Podaj liczbe n:"))
sinusy = []
for i in range(1,n+1,1):
    sinusy += [sin(i)]
print(f"sin({i}) = ",sin(i))
print(max(sinusy))
print(min(sinusy))