from math import factorial
l1 =[]
l2 =[]
for x in range(1,100+1):
 l1.append(1/x)
pass
print(sum(l1))
print(min(l1))
print(max(l1))
liczba = 1000
n= factorial(liczba)
sn = str(n)
ln = list(sn)
ls = [int(i) for i in ln]
print(sum(ls))
pass 