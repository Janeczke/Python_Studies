l=[]
l = l +[4.6]
print(l)
l2 = []
for n in range(1,10+1):
    l2+=[n**2]
print(l2)
for n in range(1,10+1):
    if n%2==0:
        l2[n-1]*= -1
print(l2)