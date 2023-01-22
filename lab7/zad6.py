def sor(l):
    ls = l.split()
    n = len(l)
    for i in range(len(ls)):
        for j in range(0, len(ls)-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                
    print(ls)
    s=len(ls)
    while s > 0:
        c = 0
        for i in range(s - 1):
            if len(ls[i]) > len(ls[i + 1]):
              c = ls[i]
            ls[i] = ls[i + 1]
            ls[i + 1] = c
        s -= 1
    print(ls)

lst = str(input("Podaj zdanie: "))
lst = sor(lst)
