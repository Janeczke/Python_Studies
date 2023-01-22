import random

lista2=[]
for i in range(10):
 lista2.append(random.randint(1,100))
print(lista2)

def sortowanie_babelkowe(lista):
    n = len(lista)
    
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True

        n -= 1

        if zamien == False: break

    print(lista)   

sortowanie_babelkowe(lista2)