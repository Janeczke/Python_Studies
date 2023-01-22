l = [3,'alfa',2.71,'kot']
print(l)
print(l[0])
print(l[-1])
l[0] = 4
l[-1]='pies'
print(l)
l2 = l
l3 = l.copy()
l[0] = 5
print(l)
print(l2)
print(l3)