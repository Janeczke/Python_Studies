print("Zadanie6")
def sortuj(lista, p):
    n = len(lista)
    if p == 0:
        st = ' '.join(lista)
        st = st.upper()
        l = st.split()
        while n > 0:
            c = 0
            for i in range(n-1):
                if l[i] > l[i+1]:
                    d = l[i]
                    c = lista[i]
                    l[i] = l[i+1]
                    lista[i] = lista[i+1]
                    l[i+1] = d
                    lista[i+1] = c
            n -= 1
    else:
        while n > 0:
            c = 0
            for i in range(n-1):
                if len(lista[i]) > len(lista[i+1]):
                    c = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = c
            n -= 1
            
s = input('podaj zdanie: ')
l1 = s.split()
sortuj(l1, 0)
print(' '.join(l1))
sortuj(l1, 1)
print(' '.join(l1)) 