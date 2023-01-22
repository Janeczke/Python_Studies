from math import factorial
an = [['' for _ in range(2)]for _ in range(100)]
liczba = 1000
n= factorial(liczba)
ls = str(n)
for _id in range(100):
     if _id <10:
        an[_id][0] = ''.join('0'+str(_id))
        an[_id][1] = ls.count(str(an[_id][0]))
else:
        an[_id][0] = ''.join(str(_id))
        an[_id][1] = ls.count(str(an[_id][0]))
print(f'{an[_id][0]} występuje {an[_id][1]} razy')
pass 