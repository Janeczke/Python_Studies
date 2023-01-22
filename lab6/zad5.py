l1 = []
l2 = []
for x in range(30+1):
 l1.append((3**x)-(2**x))
for x in l1:
 l2.append(x%19)
n =input('podaj n (0-18)>>')
n = int(n)
if n in l2:
 print(f'{n} występuje {l2.count(n)} razy')
else:
 print('nie ma tej liczby w l2')