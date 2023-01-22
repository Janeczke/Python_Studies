sinus = []
sqrts = []
from math import sqrt, sin
for x in range(1,20+1):
    sqrts.append(sqrt(x))
    sinus.append((sin(x)))

for x in sinus:
    print(x)
print()
for x in sqrts:
    print(x)