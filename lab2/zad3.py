n=int(input("Podaj pierwszą zmienną: "))
m=int(input("Podaj drugą zmienną: "))

if(n<m):
    x=range(n, m+1)
    for i in x:
        print(i, end=" ")

if(n>m):
    y=range(n, m-1, -1)
    for i in y:
        print(i, end=" ")