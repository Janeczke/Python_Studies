import random
l = []
pom = 0
random.seed()
for i in range(10):
    l += [random.randint(0,100)]
print(f'l1 = {l}')
l2 = l.copy()
l2+=[l[0]]
del l2[0]
l3 = l.copy()
l3.insert(0, l[-1])
del l3[-1]
l4 = l.copy()[::-1]
l5 = l.copy()
while pom < len(l5):
    if l5[pom]%2==0: pom+=1
    else: del l5[pom]
l6 = l.copy()
pom=0
while pom< len(l6):
    if pom % 2 != 0:
        l6[pom] = -1
        if l6[pom] % 2 == 0: l6[pom]=-1
    if l6[pom] % 2 == 0: l6[pom]=-1
    pom+=1
pom =0
while pom < len(l6):
    if l6[pom] == -1:
        del l6[pom]
    else:
        pom+=1
print(f'l2 = {l2}')
print(f'l3 = {l3}')
print(f'l4 = {l4}')
print(f'l5 = {l5}')
print(f'l6 = {l6}')