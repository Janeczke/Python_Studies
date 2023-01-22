import math
def pier(n):
    k=1
    for i in range(1, n // 2 + 1):
        if (n % i == 0):
                k+=1
    if k != 2 or (n == 1 and n == 0):
        return False
    else:
        return True
fo=open('Liczby pierwsze.txt','r')
w = 0
for line in fo:
        w = line.split(" ")
print(w[-2])
fo.close()
lastNum=int(w[-2])
fo=open('Liczby pierwsze.txt','a')
for n in range(round(lastNum, -2),round(lastNum, -2)+100):
        if pier(n) is True:
                fo.write(str(n))
fo.write(" ")
fo.close()