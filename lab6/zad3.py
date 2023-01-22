from math import factorial
i = 321
si = str(i)
li=list(si)
print(li)
liczba = 1000
n=factorial(liczba)
sn = str(n)
ln = list(sn)
ile = [[0 for _ in range(2)]for _ in range(10)]
for i in range(10):
    ile[i][0] = i
for i in range(10):
    ile[i][1] = ln.count(str(i))
print(f'W {liczba}! ')
for x in range(10):
    if ile[x][1]!=0:
        print(f'{ile[x][0]} wystąpiło: {ile[x][1]}') 